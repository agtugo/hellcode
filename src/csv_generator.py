import csv


def generate_csv(csv_filename, rows):
    """Generate a CSV file from given rows."""
    with open(csv_filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ CSV file generated: {csv_filename}")
