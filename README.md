# 🧰 CLI ListManager

A clean and minimal command-line To-Do/Task Manager built with Python, Typer, and Rich — developed as part of my **July 2025 Trinity Developer Foundations** learning phase.

This project was my hands-on way to understand how real software is structured, built, and maintained. I kept it simple, modular, and focused — no unnecessary features, just what a CLI task manager needs.

---

## 📦 Features (v1.0)

✅ Lightweight JSON-based persistence  
✅ Clear command structure using Typer  
✅ Beautiful CLI tables with Rich  
✅ Modular code split across logic, CLI, and styling  
✅ Git-based solo team-style workflow (3 dev roles)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/guna2007/July-Project.git
cd July-Project

# Run commands using Python
python tm.py [command] [options]
```

---

## 🛠️ Features & Usage

Below are the implemented features with example CLI commands:

### 1. 📋 View Tasks

Displays all tasks in a Rich-formatted table.

```bash
python tm.py show
```

### 2. ➕ Add Task

```bash
python tm.py add "Complete Python CLI project" "Work"
python tm.py add "Submit assignment" "School" --date-due "30/07/2025::18:00" --id 101
```

### 3. ✅ Mark as Completed

```bash
python tm.py complete 2
```

### 4. 🗑️ Delete Task

```bash
python tm.py delete 3
```

### 5. ✏️ Update Task

```bash
python tm.py update 2 --task "Update README" --category "Docs" --date-due "30/07/2025::20:00"
```

### 6. 🧹 Clear All Tasks

```bash
python tm.py clear
```

---

## 📁 Project Structure

```bash
July-Project/
│
├── tm.py         # Main CLI using Typer
├── tasks.py      # Task class and logic
├── data.py       # Load/Save tasks from JSON
├── data.json     # Local persistent store
├── README.md     # Documentation
└── screenshots/  # Screenshots of CLI in action
```

---

## 🧠 Concepts Covered in July 2025

This mini project was the culmination of my July 2025 Developer Foundations learning phase. It integrates the following concepts:

### ✅ Python

- Data types, functions, modules
- File I/O with JSON
- OOP (Task class, methods, object creation)
- Exception handling

### ✅ CLI Tools

- Typer for command parsing
- Typer decorators: @app.command(), positional and optional arguments

### ✅ Rich Library

- Rich tables for visual output
- Color highlights, status symbols

### ✅ Git & GitHub

- git init, commit, branch, push
- Simulated solo-team workflow with 3 dev roles
- Structured project development using Git

---

## 📅 July 2025: Trinity Project Summary

| Week | Focus                          | Topics Learned                          | Progress           |
| ---- | ------------------------------ | --------------------------------------- | ------------------ |
| 1    | Python Core + Loops            | Data types, conditionals, functions     | ✅ Completed       |
| 2    | Git, Markdown, CLI Basics      | Git CLI, GitHub, Markdown README        | ✅ Completed       |
| 3    | Typer, Rich, OOP in Python     | Typer, Rich, OOP design, exceptions     | ✅ Completed       |
| 4    | CLI Mini Project – ListManager | Architecture, styling, UX, modular code | ✅ MVP Done (v1.0) |

---

## 💡 Design Goals

- Clean UX with helpful table formatting
- Easily extensible structure
- Local file-based task persistence
- Learn by doing — not just following tutorials

---

## 🧱 Built With

- Python
- Typer
- Rich
- Git
- VS Code + GitHub

---

## 📸 Screenshots

Add your screenshots here:

- screenshots/view_table.png
- screenshots/add_command.png
- screenshots/completed_output.png

Reference them in your README using relative paths like:

```markdown
![Task View](screenshots/view_table.png)
```

---

## 🙌 Final Thoughts

This project taught me how to build something real from scratch — not just code, but structure, collaboration, and clarity. I kept it minimal on purpose, and every feature was added with intent. No fluff, just function.
