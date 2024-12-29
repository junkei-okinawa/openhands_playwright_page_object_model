---
name: repo
agent: CodeAct
---
Repository: e2e-test-automation
Description: Playwrightを使用したE2Eテストを自動化するPythonプロジェクトです。与えられたURLからHTMLを解析し、Page Object Modelのコードを自動生成します。
Directory Structure:
- tests/: E2Eテストスクリプトを格納するディレクトリ
- pages/: Page Object Modelのクラスを格納するディレクトリ
- utils/: ユーティリティ関数などを格納するディレクトリ

Setup:
### 1-1. install [uv](https://docs.astral.sh/uv/getting-started/installation/)
An extremely fast Python package and project manager, written in Rust.
- macOS and linux
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```
- `uv sync`を実行して依存関係をインストールします。
- `uv run playwright install --with-deps chromium`を実行してPlaywrightのブラウザバイナリをインストールします。
- `uv venv`を実行して仮想環境を作成します。
- `source .venv/bin/activate`を実行して仮想環境を有効化します。

Guidelines:
- テストスクリプトは`tests/`ディレクトリに配置します。
- 各テストケースは、対応するページのPage Object Modelクラスを使用します。
- Page Object Modelクラスは`pages/`ディレクトリに配置します。
- 可能な限りType Hintを記述します。
- 新しい機能を追加する際は、必ずE2Eテストを追加します。
- `git add`を実行する際には、必ず対象となるファイルを指定すること。
- `git commit`を実行する際には、必ず`-m`オプションを指定し適切な`commit message`を記述すること。

Examples:
- 新しいテストケースを追加する
  1. `tests/`ディレクトリに新しいテストスクリプトファイルを作成します。
  2. テスト対象のページに対応するPage Object Modelクラスを`pages/`ディレクトリに作成します。
  3. テストスクリプト内でPage Object Modelクラスを使用して、テストシナリオを実装します。
- Page Object Modelクラスを作成する
  1. `pages/`ディレクトリに新しいPythonファイルを作成します。
  2. ファイル内で、ページに対応するPage Object Modelクラスを定義します。
  3. クラス内には、ページ上の要素にアクセスするためのメソッドを定義します。
