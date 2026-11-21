# Smart Study & Task Manager

A modular command-line (CLI) task management application built with Python. It helps students and developers organize daily study and personal tasks with persistent JSON storage.

## Features

- **Add Tasks:** Create tasks with a title, category, priority level (`Low`, `Medium`, `High`), and due date.
- **View All Tasks:** Display all saved tasks with their ID, category, priority, due date, and completion status (`Pending` or `Done`).
- **Complete Tasks:** Mark specific tasks as completed using their unique ID.
- **Delete Tasks:** Remove tasks by ID with safe input validation.
- **Persistent Storage:** Automatically saves and loads tasks using a local JSON file (`tasks.json`).

## Project Structure

```text
smart-task-manager/
├── models.py      # Task data model and dictionary serialization
├── storage.py     # JSON file reading and writing logic
├── manager.py     # Core business logic (add, view, complete, delete tasks)
├── main.py        # Terminal user interface (CLI menu and input validation)
└── tasks.json     # Auto-generated local JSON database (ignored in Git)
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MellahNadir/smart-task-manager.git
   cd smart-task-manager
   ```

2. Run the application (requires Python 3.8+):
   ```bash
   python3 main.py
   ```