selenium template
==

Docker-composeによるSelenium(Pythonバージョン)のテンプレート。

## ライセンス
MIT

## 使い方

1. 各種設定を変更
1. docker-compose up -d chrome
1. 各種テストを記述
1. docker-compose up test

テストコード `tests/spec` 以下に記述してください。  
print等の出力は `tests/output` 以下に生成されます。

TODO: デバッガは要検討。

## domの取得
`utils.browser`と`utils.element`に用意しています。

以下のように記述できます。

```python
from utils.browser import Browser

browser = Browser()

# 指定URLへ移動
browser.navigate_to('https://example.com/')

# ドキュメントルート(HTMLタグ)を取得
document = browser.document()

# idで検索(getElementById)
element = document.find_by_id('id')

# inputのvalueを取得
value = element.get_value()

# ブラウザのスクリーンショットを保存
browser.screen_shot('sample')
```

※Browserは何度インスタンス化しても問題ありません。

## ログの保存
`utils.log`に用意しています。

```python

from utils.log import Log

# ログを残すレベルの指定
Log.set_level(Log.ERROR)

Log.trace('トレースログ')   # ※ログ残らない

Log.fatal('致命的なエラー') # ※ログ残る
```

## アサーション
`assersion.expect`に用意しています。

以下のように記述できます。

```python
from assertion.expect import Assert

# 何か処理結果
actual_value = SomeFunction()

# 処理結果が期待値と等しいか判定
Assert.expect(actual_value).equals_to('期待される結果')
```

## jaモジュール
プログラマ以外が触ることも想定して、関数名などを日本語にした版を用意しています。

- utils.ja.browser
    - Browser → ブラウザ
- utils.ja.element
    - Element → 要素
- utils.ja.log
    - Log → ログ
- assertion.js.expect
    - Expect → 判定
    - Assert → 結果

それぞれjaがないモジュールと対応しています。

## 出典
https://github.com/sikkimtemi/selenium
をベースに`Dcokerfile`/`docker-compose.yml`を作成しております。

ライセンスが明記されていないので、ひとまず出典として明記しておきます。
