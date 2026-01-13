import json
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task name: ")
    category = input("Category (Study/Work/Personal): ")
    priority = input("Priority (High/Medium/Low): ")
    due_date = input("Due date (YYYY-MM-DD): ")

    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} | {task['category']} | "
              f"Priority: {task['priority']} | Due: {task['due_date']}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
