import markdown
import os


def convert_markdown_to_html(md_path):
    """Convert Markdown file to HTML."""
    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            return markdown.markdown(f.read())
    return ""
