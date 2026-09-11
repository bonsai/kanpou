# Kanpou Conversion API

Thin Python API for the Kanpou DS pipeline.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --app-dir api --reload
```

## Endpoints

- `GET /health`
- `POST /pdf2md` — multipart PDF → Markdown
- `POST /md2json` — multipart Markdown → normalized JSON

The conversion layer intentionally stays separate from AW orchestration and source-specific provider logic.
