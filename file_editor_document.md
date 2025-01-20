# `str_replace_editor` ツール ドキュメント

`str_replace_editor` ツールは、ファイルの編集を行うためのツールです。

## コマンド一覧

### 1. `create` コマンド (ファイル作成)

**実行コマンド:**
```
str_replace_editor --command create --path /workspace/new_file.txt --file_text "This is line 1.\\nThis is line 2.\\nThis is line 3."
```

**実行後のテキスト:**
```
This is line 1.
This is line 2.
This is line 3.
```

**備考/注意点:**
*   指定したパスにファイルが存在しない場合、新規にファイルが作成されます。
*   `file_text` で指定した内容がファイルに書き込まれます。

### 2. `str_replace` コマンド (文字列置換)

`str_replace` コマンドは、ファイル内の文字列を置換するためのコマンドです。

#### 2.1 基本的な置換

- **コマンド:** `str_replace`
- **オプション:** `--old_str`, `--new_str`
- **実行前のテキスト:**
    ```
    This is line 1.
    This is line 2.
    This is line 3.
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command str_replace --path /workspace/new_file.txt --old_str "This is line 2." --new_str "Modified line 2."
    ```
- **実行後のテキスト:**
    ```
    This is line 1.
    Modified line 2.
    This is line 3.
    ```
- **備考/注意点:** `old_str` に一致する最初の文字列が行単位で検索され、`new_str` に置換されます。

#### 2.2 `line_numbers` オプション

- **コマンド:** `str_replace`
- **オプション:** `--old_str`, `--new_str`, `--line_numbers`
- **実行前のテキスト:**
    ```
    This is line 1.
    Modified line 2.
    This is line 3.
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command str_replace --path /workspace/new_file.txt --old_str "This is line" --new_str "Line" --line_numbers [1, 3]
    ```
- **実行後のテキスト:**
    ```
    Line 1.
    Modified line 2.
    Line 3.
    ```
- **備考/注意点:** `line_numbers` で指定した行番号の行のみが置換対象となります。行番号は1から始まります。

#### 2.3 `line_all` オプション

- **コマンド:** `str_replace`
- **オプション:** `--old_str`, `--new_str`, `--line_all`
- **実行前のテキスト:**
    ```
    Line 1.
    Modified line 2.
    Line 3.
    Line 1.
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command str_replace --path /workspace/new_file.txt --old_str "Line 1." --new_str "Replaced Line 1." --line_all true
    ```
- **実行後のテキスト:**
    ```
    Replaced Line 1.
    Modified line 2.
    Line 3.
    Replaced Line 1.
    ```
- **備考/注意点:** `line_all=True` を指定すると、ファイル内のすべての `old_str` に一致する文字列が行単位で検索され、`new_str` に置換されます。

#### 2.4 `regex` オプション

- **コマンド:** `str_replace`
- **オプション:** `--old_str`, `--new_str`, `--regex`, `--line_all` (または `--line_numbers`, `--start`, `--end`)
- **実行前のテキスト:**
    ```
    Replaced Line 1.
    Modified line 2.
    Line 3.
    Replaced Line 1.
    ```

- **実行コマンド:**
    ```bash
    str_replace_editor --command str_replace --path /workspace/new_file.txt --old_str "^Replaced.*$" --new_str "Regex Replaced Line" --regex True
    ```
- **実行後のテキスト:**
    ```
    Regex Replaced Line
    Modified line 2.
    Line 3.
    Regex Replaced Line
    ```

- **備考/注意点:** `regex=True` を指定すると、`old_str` が正規表現として扱われ、行単位でマッチングが行われます。`line_all` オプションと組み合わせて使用することで、複数行を置換できます。

#### 2.5 `regex` および `line_all` オプション

- **コマンド:** `str_replace`
- **オプション:** `regex`, `line_all`
- **実行前のテキスト:**
    ```
    Replaced Line 1.
    Modified line 2.
    Line 3.
    Replaced Line 1.
    ```

- **実行コマンド:**
    ```bash
    str_replace_editor --command str_replace --path /workspace/new_file.txt --old_str "^.*Line.*$" --new_str "Regex Replaced Line" --regex True --line_all True
    ```
- **実行後のテキスト:**
    ```
    Regex Replaced Line
    Regex Replaced Line
    Regex Replaced Line
    Regex Replaced Line
    ```

- **備考/注意点:** `regex=True` と `line_all=True` の両方を指定すると、ファイル内のすべての行に対して `old_str` が正規表現としてマッチングされ、マッチした行が `new_str` に置換されます。

### 3. `insert` コマンド (行挿入)

- **コマンド:** `insert`
- **オプション:** `--new_str`, `--insert_line`
- **実行前のテキスト:**
    ```
    Regex Replaced Line
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command insert --path /workspace/new_file.txt --new_str "Inserted Line" --insert_line 1
    ```
- **実行後のテキスト:**
    ```
    Regex Replaced Line
    Inserted Line
    ```
- **備考/注意点:** 指定した行番号の**後**に新しい行が挿入されます。行番号は1から始まります。

### 4. `delete` コマンド (行削除)

#### 4.1 `delete_lines` オプション

- **コマンド:** `delete`
- **オプション:** `--delete_lines`
- **実行前のテキスト:**
    ```
    Regex Replaced Line
    Inserted Line
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command delete --path /workspace/new_file.txt --delete_lines [1]
    ```
- **実行後のテキスト:**
    ```
    Inserted Line
    ```
- **備考/注意点:** `delete_lines` で指定した行番号の行が削除されます。行番号は1から始まります。

#### 4.2 `start` と `end` オプション

- **コマンド:** `delete`
- **オプション:** `--start`, `--end`
- **実行前のテキスト:**
    ```
    Inserted Line
    Another Line
    Yet Another Line
    Last Line
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command delete --path /workspace/new_file.txt --start 2 --end 3
    ```
- **実行後のテキスト:**
    ```
    Inserted Line
    Last Line
    ```
- **備考/注意点:** `start` から `end` までの行番号の行が削除されます。行番号は1から始まります。

### 5. `view` コマンド (ファイル表示)

#### 5.1 ファイル全体を表示

- **コマンド:** `view`
- **オプション:** (なし)
- **実行前のテキスト:**
    ```
    Inserted Line
    Last Line
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command view --path /workspace/new_file.txt
    ```
- **実行後のテキスト:**
    ```
    Inserted Line
    Last Line
    ```
- **備考/注意点:** ファイルの内容がすべて表示されます。

#### 5.2 `view_range` オプション

- **コマンド:** `view`
- **オプション:** `--view_range`
- **実行前のテキスト:**
    ```
    Inserted Line
    Last Line
    ```
- **実行コマンド:**
    ```bash
    str_replace_editor --command view --path /workspace/new_file.txt --view_range [1, 2]
    ```
- **実行後のテキスト:**
    ```
    Inserted Line
    Last Line
    ```
- **備考/注意点:** `view_range` で指定した行範囲が表示されます。行番号は1から始まります。

### 6. `undo_edit` コマンド (編集取り消し)

- **コマンド:** `undo_edit`
- **オプション:** (なし)
- **実行前のテキスト:** (編集操作後の状態)
- **実行コマンド:**
    ```bash
    str_replace_editor --command undo_edit --path /workspace/new_file.txt
    ```
-  **実行後のテキスト:** (直前の編集操作前の状態)
- **備考/注意点:** 直前の編集操作が取り消されます。

**注意点:**
複数行にわたる長文を編集する場合は、`str_replace`コマンドでエラーが発生しやすいです。そのような場合は、`execute_bash`の`rm`コマンドでファイルを削除し、`file_editor`の`create`コマンドで修正後の内容でファイルを再作成することを推奨します。