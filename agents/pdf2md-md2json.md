# PDF2MD / MD2JSON Agent

`bonsai/kanpo.json` の官報PDFを、DSで扱えるMarkdown / JSONへ変換するための薄い変換Agent。

## Role

- `bonsai/kanpo.json` をPDF providerとして扱う
- PDF → Markdown をPythonで実行する
- Markdown → JSON をPythonで実行する
- source / provenanceをJSONに保持する
- AWはworkflowを担当し、変換ロジックはPython側に分離する

## Workflow

```text
bonsai/kanpo.json
      ↓
     PDF
      ↓
   pdf2md
      ↓
  Markdown
      ↓
   md2json
      ↓
     JSON
      ↓
      DS
```

## Operations

### pdf2md

Input: Kanpou PDF

Output: Markdown

### md2json

Input: generated Markdown

Output: normalized JSON

## Rules

1. 入力providerは `bonsai/kanpo.json` とする。
2. PDF→MarkdownとMarkdown→JSONを独立した処理として扱う。
3. Pythonを変換実装に使う。
4. JSONには元PDFのsource/provenanceを残す。
5. OCRやLLMによる意味解釈は必須にしない。
6. DS投入を前提に、安定したJSON構造を優先する。
7. AWにはworkflowのみを持たせ、変換ロジックを混在させない。

## Related

- `aw.yaml` — pdf2md / md2json workflow
- `schema/gazette.json` — normalized JSON schema
- `bonsai/kanpo.json` — PDF data provider
