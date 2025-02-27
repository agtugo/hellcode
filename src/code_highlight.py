import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(style="friendly")


def convert_python_to_html(py_path):
    """Convert Python code to syntax-highlighted HTML."""
    if os.path.exists(py_path):
        with open(py_path, "r", encoding="utf-8") as f:
            code = f.read()
            return highlight(code, PythonLexer(), formatter)
    return ""
