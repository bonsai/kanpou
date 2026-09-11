# 官報テキスト / データセット候補

DS用途を優先して、既存資源をprovider候補として整理する。

## 1. 官報検索ソフト

PDF → JPG → Tesseract OCR → テキスト整形 → SQLite → 全文検索、という実装例。

- Source: Vector「官報検索ソフト」
- URL: https://www.vector.co.jp/soft/winnt/net/se524660.html
- 特徴: Internet版官報を一括取得し、OCR結果をSQLiteに格納して全文検索。
- 用途: **SQLite schema / OCR pipeline の参考実装**
- 注意: 配布データそのものをkanpouへ取り込む前に利用条件を確認する。

## 2. TB3DS

官報PDFをPoppler + Tesseractでテキスト化し、GREP可能な状態にする実例。

- Repository: https://github.com/GinSanaduki/TB3DS
- 特徴: PDF → PNG → Tesseract → text / 行志向データへの変換。
- 用途: **OCR精度・前処理・テキスト化の参考**
- 注意: 特定の官報記事を対象としたプロジェクトなので、全文DBとは区別する。

## 3. kanpo-downloader

2025年4月以降の官報PDFを年別GitHub repositoryへ蓄積。

- Organization: https://github.com/kanpo-downloader
- Repository: https://github.com/kanpo-downloader/kanpo-downloader.github.io
- Data repositories: `kanpo-2025`, `kanpo-2026` など
- 用途: **公式PDFの再現可能なraw provider**
- 注意: PDF archiveであり、正規化済みテキストDBではない。

## 4. 公式官報

2025年4月1日以降、官報発行サイト掲載の電子データが官報の正本。

- URL: https://www.kanpo.go.jp
- 用途: **source of truth / provenance**

## 5. DS方針

自前OCRを最初から作らない。

```text
existing text/DB ─┐
existing OCR ─────┼→ provider → normalize → dataset → DS
official PDF ─────┘
```

まず既存SQLite/テキスト資源を調査し、利用可能なものはproviderとして取り込む。
公式データはprovenance用に保持し、派生テキストと混同しない。

## 次の調査

- [ ] SQLite実データを公開している実装を追加調査
- [ ] GitHub上の官報OCR全文データを追加調査
- [ ] 利用規約・再配布可否を確認
- [ ] 最初の小規模datasetを作成
- [ ] DuckDB / BigQuery向けschemaを設計
- [ ] 時系列・entity・topic分析をPoC化
