from manager import TaskManager


def display_menu():
    print("\n--- Smart Study & Task Manager ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            category = input("Enter category (e.g., Study, Personal): ")
            priority = input("Enter priority (Low, Medium, High): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            new_task = manager.add_task(title, category, priority, due_date)
            print(f"Task '{new_task.title}' added with ID {new_task.task_id}.")
        elif choice == "2":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "Done" if task.is_completed else "Pending"
                    print(f"[{task.task_id}] {task.title} | {task.category} | {task.priority} | Due: {task.due_date} | {status}")
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                if manager.complete_task(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if manager.delete_task(task_id):
                    print("Task deleted!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()