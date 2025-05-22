# FileSearcher Application

A simple Python application that recursively searches through a directory tree for a specified partial term in files, and outputs all matches to a JSON file.

---

## Features

* **Recursive Traversal**: Walks through all subfolders under a given root directory.
* **Substring Search**: Finds lines containing a partial term (case-sensitive or case-insensitive).
* **File Filtering**: Optionally limit the search to specific file extensions (e.g., `.py`, `.md`).
* **JSON Output**: Collects matches into a structured JSON file, including file path, line number, and line content.

---

## Prerequisites

* Python 3.6 or higher installed

---

## Installation

1. Copy the following files into your project directory:

   * `file_searcher.py`
   * `app.py`
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Windows: venv\\Scripts\\activate
   ```

---

## Configuration

### file\_searcher.py

The core logic lives in `FileSearcher`, which accepts these parameters:

* `directory` (str): Root folder to start the search.
* `term` (str): Partial term (substring) to match in each line.
* `ignore_case` (bool): If `True`, performs case-insensitive matching (default: `False`).
* `extensions` (List\[str] or `None`): List of file extensions (including the dot) to include. If `None`, all files are scanned.
* `output` (str): Path to the JSON file for results (default: `results.json`).

### app.py

An example “caller” class demonstrates how to instantiate and run the searcher. You can adjust the parameters in the `SearchApp` constructor:

```python
# app.py excerpt
self.searcher = FileSearcher(
    directory="path/to/your/folder",
    term="TODO",
    ignore_case=True,
    extensions=[".py", ".md"],
    output="todo_matches.json"
)
```

---

## Usage

### 1. Via the Example App

Run the example script directly from the command line:

```bash
python app.py
```

Upon completion, the console will report:

```
✅ Search complete! Results written to todo_matches.json
```

Open the JSON file to inspect all matches.

### 2. As a Library

Import and use `FileSearcher` within your own modules:

```python
from file_searcher import FileSearcher

searcher = FileSearcher(
    directory="./logs",
    term="ERROR",
    ignore_case=False,
    extensions=['.log'],
    output="error_matches.json"
)

result_file = searcher.run()
print(f"Results saved to {result_file}")
```

---

## JSON Output Format

The output is a JSON array of objects, each with:

* **`file_path`**: Path to the file containing the match.
* **`line_number`**: Line number where the term was found (1-based).
* **`line`**: The full text of that line (trimmed of trailing newline).

Example:

```json
[
  {
    "file_path": "src/main.py",
    "line_number": 42,
    "line": "# TODO: Implement the search feature"
  },
  {
    "file_path": "README.md",
    "line_number": 10,
    "line": "This is a TODO item in documentation."
  }
]
```

---

## Customization

* **Output Path**: Change the `output` parameter to write elsewhere.
* **Add CLI**: Wrap the logic in `argparse` or `click` in `app.py` for direct command-line use.
* **Error Handling**: Extend `_search_file` to log or handle exceptions differently.

---

## License

MIT License.
