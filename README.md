# Build Playwright Page Object Model with AI Agents

このプロジェクトは、Web UI テストをPlaywright ＆ Page Object Model (POM) で実現するためにAI Agent[OpenHands](https://github.com/All-Hands-AI/OpenHands)を使用している実験的なプロジェクトです。

## プロジェクト構成

- `pages/`: ページオブジェクトクラスが含まれています。
  - `base_page.py`: 共通のページ操作を定義するBasePageクラスが含まれています。
  - `locators.py`: ページ要素のロケータを定義するクラスが含まれています。

- `tests/`: テストスクリプトが含まれています。
  - `test_data.json`: テストデータを定義するファイルが含まれています。

- `pyproject.toml`: プロジェクトの設定ファイル。

- `requirements.txt`: プロジェクトの依存関係をリストしたファイル。

## テストの実装

テストでは、以下の機能を使用しています。

- **BasePageクラス**: ページオブジェクトクラスの共通処理をまとめた基底クラスを使用しています。
- **ロケータの一元管理**: ページ要素のロケータを`locators.py`で一元管理しています。
- **pytestフィクスチャ**: `conftest.py`で定義されたフィクスチャを使用して、ページオブジェクトの初期化を簡素化しています。
- **データ駆動テスト**: `test_data.json`ファイルを使用して、テストデータを管理しています。

## 実行方法

1. 依存関係をインストールします。
   ```bash
   uv sync
   ```

2. Playwright のブラウザバイナリをインストールします。
   ```bash
   uv run playwright install --with-deps chromium
   ```

3. allure をインストールします。
   ```bash
   sudo apt-get install -y default-jre
   wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
   sudo dpkg -i allure_2.18.1-1_all.deb
   rm allure_2.18.1-1_all.deb
   ```

4. テストを実行します。

   仮想環境内のパッケージを使用する場合は、`.venv/bin/pytest` のように直接パスを指定して実行する必要があります。
   ```bash
   .venv/bin/pytest --cov --alluredir=allure-results
   ```

5. allure レポートを確認
   ```bash
   allure serve allure-results > allure.log 2>&1 &
   ```
   上記のコマンドで `allure serve` をバックグラウンドで実行します。
   `allure.log` に出力されたURLをブラウザで開き、レポートを確認してください。
   レポート確認後、バックグラウンドで実行している `allure serve` のプロセスをkillしてください。

**Note:** テストの失敗時のみTeardownトグル内にテスト実行時の動画が添付されます

## 依存関係

- Playwright
- pytest
- allure

## Openhandsへの作業指示方法
現在、Local環境でOpenHandsサーバーを起動し、localhost:3000のフロントエンドから作業指示を行っています。

ベースとなる指示は本プロジェクトの`issue`ページの**New issue**から**work instructions**テンプレートを使って設定し、フロントエンド画面のチャットで「Github APIを使用してissue#00(番号を記載)を確認し実施せよ」と指示することで、自律的に開発が進みます。

この`README.md`も大半は AI Agent が作成したものです。

#### 考慮事項
OpenHandsが内部的に使用しているファイル編集機能がうまく機能しないことが多く、ファイル編集に失敗したり、重複する内容を入力することが多いです。うまく編集できないことに AI Agent も苛立ちを隠していません(笑)

完全自律ではファイル編集で何度も失敗し頑張ってリトライし続けてしまうことが多いので、適宜 人の介入は必要です。

[OpenHands]((https://github.com/All-Hands-AI/OpenHands)) の内部実装を確認したところ`function calling` を独自実装しているので、改善してPRを送ろうと思います。