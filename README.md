# kanpou

官報をAgentから利用するためのAPI wrapper PoC。

## Goal

公式の官報データを取得し、Agentが扱いやすい正規化JSONへ変換する。

```text
Agent
  ↓
kanpou skill
  ↓
official source
  ↓
fetch → normalize
  ↓
JSON
```

## PoC scope

- 指定日の官報を取得するための境界を定義
- 官報 issue / section / article の最小スキーマを定義
- 検索はまず取得済みデータを対象とする
- 公式データをsource of truthとする

## Non-goals

- 民間検索サービスの再実装
- 最初から全文検索基盤を作ること
- MCP専用実装にすること

## Next

1. official source adapter
2. parser / normalizer
3. local search
4. Agent skill interface
