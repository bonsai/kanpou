# kanpou Agent Skill

## Purpose

官報の公式データをAgentから取得・正規化するための薄いwrapper。

## Contract

Input:

```yaml
operation: fetch
  date: YYYY-MM-DD
```

Output:

```json
{
  "source": "official",
  "date": "YYYY-MM-DD",
  "issues": []
}
```

## Architecture

```text
Agent
 ↓
kanpou skill
 ↓
source adapter
 ↓
fetch
 ↓
normalize
 ↓
JSON
```

## Rules

- 公式ソースを優先する
- provider固有のレスポンスをAgentへ漏らさない
- source metadataを保持する
- 最小PoCから開始し、検索・MCP等は後付けする

## Future operations

- `fetch`
- `search`
- `get_issue`
- `get_article`
