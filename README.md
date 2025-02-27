# 🚀 Hellcode Patterns – Welcome to the Hell of DSA Studying! 🔥
**A structured Anki deck to master Data Structures and Algorithms (DSA) patterns efficiently.**  
Feel free to study, contribute, and improve your problem-solving skills!

## 📌 About the Project
Hellcode Patterns is a curated **Anki deck** designed to help you learn and **memorize common problem-solving patterns**.  
It covers **fundamental patterns, common problems, and miscellaneous DSA concepts**.

Each card follows a structured format:
- **Topic & Description**
- **Iterative Steps + Code**
- **Recursive Steps + Code (if applicable)**

The goal is to make **efficient recall possible** through spaced repetition.

---

## 📦 Anki Deck Structure
The deck is split into **three models**, ensuring that only relevant cards are generated:

| Model                 | Model ID     | Fields                                      |
|-----------------------|-------------|---------------------------------------------|
| **Description Model** | `1590995667` | `Topic`, `Description`, `Tags`             |
| **Iterative Model**   | `1134111604` | `Topic`, `Iterative Steps`, `Code`, `Tags` |
| **Recursive Model**   | `1420682326` | `Topic`, `Recursive Steps`, `Code`, `Tags` |

---

## 🚀 How to Generate the Anki Deck
This repository contains a script to **automatically generate the deck** from markdown files.

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed, then set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### **2️⃣ Generate the Anki Deck**
Run the following command to process all markdown files and create the `.apkg` Anki deck:

```bash
python src/generate_anki.py
```

### **3️⃣ Import into Anki**
- Open **Anki**.
- Go to **File → Import**.
- Select the generated `anki_deck.apkg`.
- Start studying!

---

## 🔧 Project Structure
```
hellcode/
├── README.md                # Project documentation
├── requirements.txt         # Dependencies for Anki generation
├── cards/                   # Contains all flashcards
│   ├── fundamentals/        # Core DSA patterns
│   ├── common_problems/     # Well-known coding problems
│   ├── miscellaneous/       # Other useful patterns
│   ├── machine_learning/    # (Optional) ML-related cards
├── src/                     # Source code for Anki generation
│   ├── generate_anki.py     # Main script to generate the deck
│   ├── anki_exporter.py     # Handles Anki deck creation
│   ├── utils.py             # Helper functions
├── output/                  # Generated Anki deck
│   ├── anki_deck.apkg       # Final Anki file
│   ├── anki_deck.csv        # CSV export (optional)
```

---

## 🤝 Contributing
We welcome contributions! If you want to add new cards, improve existing ones, or fix issues, follow these steps:

### **✅ 1. Fork the Repository**
If you're not a collaborator, click **"Fork"** at the top-right of this repo on GitHub.  
This creates a **copy of the repo under your GitHub account**.

### **✅ 2. Clone Your Fork**
After forking, clone the repo to your local machine:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/hellcode.git
cd hellcode
```

### **✅ 3. Create a New Branch**
Even in your fork, it’s good practice to work in a **separate branch**:

```bash
git checkout -b feature/new-pattern
```

### **✅ 4. Add or Modify Cards**
- Navigate to `cards/` and add a new markdown file for a new pattern.  
- Follow the existing structure.
- Run `generate_anki.py` to test.

### **✅ 5. Commit and Push Your Changes**
Once you're happy with the changes, commit and push:

```bash
git add .
git commit -m "Added new pattern: XYZ"
git push origin feature/new-pattern
```

### **✅ 6. Open a Pull Request (PR)**
- Go to your forked repo on GitHub.
- Click **"Compare & pull request"**.
- Fill in details and submit the PR.

We’ll review it and merge it if everything looks good! 🚀

---

## **💡 FAQ**
### ❓ Can I add my own Anki cards?
Yes! Just add a markdown file to `cards/`, following the existing structure.

### ❓ What happens if I update my deck in Anki?
If you **re-import a modified deck**, Anki should update cards instead of creating duplicates.

### ❓ How can I filter only beginner-friendly cards?
Anki allows filtering using **tags**. You can filter cards by `easy`, `medium`, `hard`, etc.

---

## 📢 Final Thoughts
This project aims to **help developers systematically master algorithms and problem-solving techniques**.  
We encourage contributions to keep improving the deck and making studying **more efficient for everyone!**

🔥 **Happy Coding!** 🔥
