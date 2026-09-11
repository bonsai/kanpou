from __future__ import annotations

import io
import re
from datetime import datetime, timezone

from fastapi import FastAPI, File, HTTPException, UploadFile
from pypdf import PdfReader

app = FastAPI(title="kanpou conversion API", version="0.1.0")


def pdf_to_markdown(data: bytes) -> str:
    try:
        reader = PdfReader(io.BytesIO(data))
        pages = []
        for index, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            pages.append(f"## Page {index}\n\n{text}")
        return "\n\n".join(pages).strip()
    except Exception as exc:
        raise HTTPException(status_code=422, detail=f"PDF extraction failed: {exc}") from exc


def markdown_to_json(markdown: str, source: str | None = None) -> dict:
    lines = markdown.splitlines()
    pages = []
    current = None
    buffer = []

    def flush() -> None:
        nonlocal current, buffer
        if current is None:
            return
        pages.append({"page": current, "text": "\n".join(buffer).strip()})
        buffer = []

    for line in lines:
        match = re.match(r"^## Page (\d+)\s*$", line.strip())
        if match:
            flush()
            current = int(match.group(1))
        else:
            buffer.append(line)
    flush()

    return {
        "source": source or "api",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pages": pages,
    }


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/pdf2md")
async def pdf2md(file: UploadFile = File(...)) -> dict:
    if file.content_type not in ("application/pdf", "application/octet-stream"):
        raise HTTPException(status_code=415, detail="PDF file required")
    data = await file.read()
    markdown = pdf_to_markdown(data)
    return {"filename": file.filename, "markdown": markdown}


@app.post("/md2json")
async def md2json(file: UploadFile = File(...)) -> dict:
    if file.content_type not in ("text/markdown", "text/plain", "application/octet-stream"):
        raise HTTPException(status_code=415, detail="Markdown file required")
    data = await file.read()
    try:
        markdown = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise HTTPException(status_code=400, detail="Markdown must be UTF-8") from exc
    return markdown_to_json(markdown, file.filename)
