# app.py

from file_searcher import FileSearcher

class SearchApp:
    def __init__(self):
        self.searcher = FileSearcher(
            directory=r"C:\Users\sergioy\python",
            term="TODO",
            ignore_case=True,
            extensions=[".py", ".md"],
            output="todo_matches.json"
        )

    def perform_search(self):
        result_json = self.searcher.run()
        print(f"✅ Search complete! Results written to {result_json}")

if __name__ == "__main__":
    SearchApp().perform_search()
