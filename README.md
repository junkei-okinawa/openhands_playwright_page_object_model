# Playwright Page Object Model の例

このプロジェクトは、Playwright を使用した Web UI テストにおける Page Object Model (POM) の使用例を示しています。

## プロジェクト構成

- `openhands_playwright_page_object_model/`: プロジェクトの主要ファイルが含まれています。
  - `__init__.py`: このディレクトリを Python パッケージにするための空ファイル。
  - `main.py`: テストを実行するためのメインスクリプト。
  - `pages/`: ページオブジェクトクラスが含まれています。
  - `tests/`: テストスクリプトが含まれています。
  - `pyproject.toml`: プロジェクトの設定ファイル。
  - `requirements.txt`: プロジェクトの依存関係をリストしたファイル。
  - `uv.lock`: 依存関係のロックファイル。

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

## 依存関係

- Playwright
- pytest

## 貢献
プルリクエストを送信して、このプロジェクトに貢献してください。
