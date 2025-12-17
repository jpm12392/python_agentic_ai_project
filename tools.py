def calculator(expression: str) -> str:
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {e}"


def search(query: str) -> str:
    # Mock search (replace with real API if needed)
    return f"Search result for '{query}': Python is a popular programming language."
