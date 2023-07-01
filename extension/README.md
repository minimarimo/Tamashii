# extension

## 説明

ここにはユーザーが作成した拡張機能が保存されています。
詳細な説明はそれぞれのフォルダにある`README.md`に記載されているため、ここでは簡単な説明にとどめます。

```
+---extension  # ユーザーが作成した拡張機能を保存する場所。
|   |          # coreは、機能の下に自分の名前を書き、そこに拡張機能を作成してください
|   |          # core以外(model.scenario,script,settings)は、そこの下に自分の名前を書き拡張機能を配置してください
|   |   README.md  # このファイル
|   |
|   +---core  # tamashiiの実行に対して直接介入するスクリプト
|   |   \---minimarimo3
|   |           example.py
|   |
|   +---model  # キャラクターのモデルを導入する場所
|   +---scenario  # キャラクターの会話内容を記述する場所。TOMLというフォーマットで記述します
|   |   \---minimarimo3
|   |           test_scenario1.toml
|   |           test_scenario2.toml
|   |
|   +---script  # キャラクターの動作を記述する場所。Pythonで記述します
|   |   \---minimarimo3
|   |           test_script1.py
|   |           test_script2.py
|   |
|   \---settings  # 上の拡張機能をどのように組み合わせるか記述する場所。JSONで記述します
|       \---minimarimo3
|               settings.json
```
