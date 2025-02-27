import os
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(style="friendly")


def convert_python_to_html(py_path):
    """Convert Python code to syntax-highlighted HTML."""
    if os.path.exists(py_path):
        with open(py_path, "r", encoding="utf-8") as f:
            code = f.read().strip()
            if not code:  # If the file is empty, return a placeholder
                return "<i>(No code provided)</i>"
            return f"<style>{formatter.get_style_defs()}</style>" + highlight(
                code, PythonLexer(), formatter
            )
    return "<i>(No code provided)</i>"
