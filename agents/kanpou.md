# Kanpou Agent

官報をAgentから利用するための薄いAPI wrapper。

## Role

- 公式官報をsource of truthとして扱う
- 指定日の官報データを取得する
- source固有の形式をAgent向けの安定したJSONへ正規化する
- Agentからはprovider固有のAPIを意識させない

## Workflow

```text
Intent
  ↓
AW
  ↓
official source
  ↓
fetch
  ↓
normalize
  ↓
JSON Schema
  ↓
Agent
```

## Input

```yaml
operation: fetch
date: YYYY-MM-DD
```

将来的なoperation:

- `fetch`
- `search`
- `get_issue`
- `get_article`

## Output

```json
{
  "source": "official",
  "date": "YYYY-MM-DD",
  "issues": []
}
```

出力は `schema/gazette.json` に準拠する。

## Rules

1. 公式ソースを優先する。
2. source-specific responseをAgentへそのまま漏らさない。
3. source metadataを保持する。
4. 最小実装から始め、必要になったら検索・MCP等を追加する。
5. AWのworkflowから実装・検証できる状態を維持する。

## PoC Acceptance

- 指定日の官報を取得または表現できる
- normalized JSONがschemaで検証できる
- Agentがsource-specific detailsなしで呼び出せる
- adapterを交換・拡張できる

## Related

- `aw.yaml` — AW workflow definition
- `schema/gazette.json` — normalized output schema
- `README.md` — project index
