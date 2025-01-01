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

3. allure-framework のインストール
```bash
sudo apt-get install -y default-jre
wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
sudo dpkg -i allure_2.18.1-1_all.deb
rm allure_2.18.1-1_all.deb
33. rm allure_2.18.1-1_all.deb install_jre.log

# インストールできているか確認
allure --version
```
4. テストを実行します。
   ```bash
   uv run pytest tests/ --alluredir=allure-results
   ```

5. allure レポートを確認
   ```bash
   allure serve allure-results &
   Generating report to temp directory...
   # Report successfully generated to /tmp/4283537111202696799/allure-report
   # Starting web server...
   # 2024-12-30 07:38:20.548:INFO::main: Logging initialized @788ms to org.eclipse.jetty.util.log.StdErrLog
   # Can not open browser because this capability is not supported on your platform. You can use the link below to open the report manually.
   # Server started at <http://192.168.215.4:42273/>. Press <Ctrl+C> to exit
   ```


## 依存関係

- Playwright
- pytest

## 貢献

プルリクエストを送信して、このプロジェクトに貢献してください。
