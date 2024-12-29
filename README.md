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
3. テストを実行します。
   ```bash
   uv run pytest tests/
   ```
4. カバレッジを計測してテストを実行します。
   ```bash
   uv run pytest-cov pytest --cov
   ```

## 依存関係

- Playwright
- pytest

## 貢献

プルリクエストを送信して、このプロジェクトに貢献してください。
