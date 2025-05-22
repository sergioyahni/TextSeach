import os
import json
from typing import List, Optional, Dict, Any

class FileSearcher:
    """
    Recursively search files under a directory for a given term,
    and write matches out to a JSON file.
    """
    def __init__(
        self,
        directory: str,
        term: str,
        ignore_case: bool = False,
        extensions: Optional[List[str]] = None,
        output: str = "results.json"
    ):
        """
        :param directory: root folder to start the search
        :param term: substring to search for in each line
        :param ignore_case: if True, perform case-insensitive matching
        :param extensions: list of file extensions to include (e.g. ['.py','.txt']), or None to include all
        :param output: path of the JSON file to write results into
        """
        self.directory = directory
        self.term = term
        self.ignore_case = ignore_case
        self.extensions = extensions
        self.output = output

    def _line_matches(self, line: str) -> bool:
        if self.ignore_case:
            return self.term.lower() in line.lower()
        return self.term in line

    def _search_file(self, file_path: str, results: List[Dict[str, Any]]) -> None:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for lineno, line in enumerate(f, start=1):
                    if self._line_matches(line):
                        results.append({
                            "file_path": file_path,
                            "line_number": lineno,
                            "line": line.rstrip()
                        })
        except Exception:
            # skip binaries or unreadable files
            pass

    def run(self) -> str:
        """
        Perform the recursive search, collect all matches, and write them to JSON.
        :returns: the path to the output JSON.
        """
        results: List[Dict[str, Any]] = []

        for root, _, files in os.walk(self.directory):
            for fname in files:
                if self.extensions and not any(fname.endswith(ext) for ext in self.extensions):
                    continue
                self._search_file(os.path.join(root, fname), results)

        with open(self.output, "w", encoding="utf-8") as jsonfile:
            json.dump(results, jsonfile, ensure_ascii=False, indent=2)

        return self.output
