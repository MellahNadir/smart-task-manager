import json
from models import Task


def save_tasks(tasks, filename="tasks.json"):
    tasks_data = []
    for task in tasks:
        tasks_data.append(task.to_dict())
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks_data, file, indent=4)


def load_tasks(filename="tasks.json"):
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks_data = json.load(file)
        for task in tasks_data:
            tasks.append(Task.from_dict(task))
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []