# Build Playwright Page Object Model with AI Agents

このプロジェクトは、Web UI テストをPlaywright ＆ Page Object Model (POM) で実現するためにAI Agent[OpenHands](https://github.com/All-Hands-AI/OpenHands)を使用している実験的なプロジェクトです。

## プロジェクト構成

- `pages/`: ページオブジェクトクラスが含まれています。
  - `base_page.py`: 共通のページ操作を定義するBasePageクラスが含まれています。
  - `docs_page.py`: `Docs` ページのページオブジェクトクラスが含まれています。
  - `enterprise_page.py`: `Enterprise` ページのページオブジェクトクラスが含まれています。
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

49      4. コードフォーマットには `black` を使用します。
    50     ```bash
    51     uv run black pages
    52     uv run black tests
    53     ```
    54  
    55  5. import 文のソートには `isort` を使用します。
    56     ```bash
    57     uv run isort .
    58     ```
    59  
    60  6. テストを実行します。
    61  
    62     仮想環境内のパッケージを使用する場合は、`uv run <package name>` のように実行します。
    63     ```bash
    64     uv run pytest --cov --alluredir=allure-results
    65     ```
   uv run pytest --cov --alluredir=allure-results
   ```

5. allure レポートを確認。allure はNo3でバイナリを直接インストールしているので`uv run`は必要ありません。
   ```bash
   allure serve allure-results > allure.log 2>&1 &
   ```
   上記のコマンドで `allure serve` をバックグラウンドで実行します。
   `allure.log` に出力されたURLをブラウザで開き、レポートを確認してください。
   レポート確認後、バックグラウンドで実行している `allure serve` のプロセスをkillしてください。

**Note:** テストの失敗時のみTeardownトグル内にテスト実行時の動画が添付されます

## Allure レポート
Allure レポートは、テスト結果を視覚的に表現し、分析を容易にするために使用されます。このプロジェクトでは、以下の Allure デコレータを使用してレポートを強化しています。

- `@allure.epic`: テストをエピックでグループ化します。
- `@allure.feature`: テストをフィーチャーでグループ化します。
- `@allure.severity`: テストの重要度レベルを設定します。
- `@allure.step`: テストをより小さく、理解しやすいステップに分割します。
- `@allure.description`: テストケースの詳細な説明を提供します。
- `@allure.id`: テストケースに一意のIDを設定します。

## 依存関係

- Playwright
- pytest
- allure

## Openhandsへの作業指示方法
現在、Local環境でOpenHandsサーバーを起動し、localhost:3000のフロントエンドから作業指示を行っています。

ベースとなる指示は本プロジェクトの`issue`ページの**New issue**から**work instructions**テンプレートを使って設定し、フロントエンド画面のチャットで「Github APIを使用してissue#00(番号を記載)を確認し実施せよ」と指示することで、自律的に開発が進みます。

この`README.md`も大半は AI Agent が作成したものです。