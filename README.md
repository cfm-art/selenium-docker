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
