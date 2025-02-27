import os
from markdown_to_html import convert_markdown_to_html
from code_highlight import convert_python_to_html
from csv_generator import generate_csv
from anki_exporter import create_anki_deck
import genanki

# Directories
base_dir = "cards/fundamentals"
output_csv = "anki_deck.csv"
output_apkg = "anki_deck.apkg"

# Prepare CSV Data
csv_rows = [
    [
        "Topic",
        "Description",
        "Iterative Steps",
        "Iterative Code",
        "Recursive Steps",
        "Recursive Code",
    ]
]
anki_notes = []

# Process all topics
for topic_folder in sorted(os.listdir(base_dir)):
    topic_path = os.path.join(base_dir, topic_folder)

    if not os.path.isdir(topic_path):
        continue

    topic_file = os.path.join(topic_path, "topic.txt")
    description_file = os.path.join(topic_path, "description.md")
    iterative_steps_file = os.path.join(topic_path, "iterative_steps.md")
    iterative_code_file = os.path.join(topic_path, "iterative_code.py")
    recursive_steps_file = os.path.join(topic_path, "recursive_steps.md")
    recursive_code_file = os.path.join(topic_path, "recursive_code.py")
    tags_file = os.path.join(topic_path, "tags.txt")

    # Read topic
    with open(topic_file, "r", encoding="utf-8") as f:
        topic = f.read().strip()
    # Read tags
    with open(tags_file, "r", encoding="utf-8") as f:
        tags = f.read().strip()

    # Convert files
    description_html = convert_markdown_to_html(description_file)
    iterative_steps_html = convert_markdown_to_html(iterative_steps_file)
    iterative_code_html = convert_python_to_html(iterative_code_file)
    recursive_steps_html = convert_markdown_to_html(recursive_steps_file)
    recursive_code_html = convert_python_to_html(recursive_code_file)

    # Add to CSV
    csv_rows.append(
        [
            topic,
            description_html or "",
            iterative_steps_html or "",
            iterative_code_html or "",
            recursive_steps_html or "",
            recursive_code_html or "",
            tags or "",
        ]
    )

    # Add to Anki
    anki_notes.append(
        [
            topic,
            description_html or "",
            iterative_steps_html or "",
            iterative_code_html or "",
            recursive_steps_html or "",
            recursive_code_html or "",
            tags or "",
        ]
    )

# Generate CSV
generate_csv(output_csv, csv_rows)

# Generate Anki deck
anki_deck = create_anki_deck("Hellcode Patterns Deck", anki_notes)
genanki.Package(anki_deck).write_to_file(output_apkg)

print(f"✅ Anki deck generated: {output_apkg}")
