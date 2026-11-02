"""Mini Task Tracker - AI Engineering, Week 1, Day 2.

A menu-based task manager that saves its tasks to tasks.json
and reloads them the next time the program runs.
"""

import json

FILENAME = "tasks.json"


def load_tasks():
    """Load tasks from tasks.json; return an empty list if the file is missing or unreadable."""
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
        print(f"Loaded {len(tasks)} saved task(s).")
        return tasks
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("tasks.json could not be read. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Write the task list to tasks.json."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Ask for a title and add it as a Pending task."""
    title = input("Task title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def view_tasks(tasks):
    """Show a numbered list of tasks with Pending/Done status."""
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def get_task_index(tasks):
    """Ask for a task number; return its list index, or None if invalid."""
    if not tasks:
        print("No tasks yet.")
        return None
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    if number < 1 or number > len(tasks):
        print(f"Invalid task number. Choose between 1 and {len(tasks)}.")
        return None
    return number - 1


def complete_task(tasks):
    """Mark the selected task as done."""
    index = get_task_index(tasks)
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("Task completed.")


def delete_task(tasks):
    """Remove the selected task."""
    index = get_task_index(tasks)
    if index is None:
        return
    tasks.pop(index)
    save_tasks(tasks)
    print("Task deleted.")


def main():
    tasks = load_tasks()  # reload saved tasks at startup
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add")
        print("2. View")
        print("3. Complete")
        print("4. Delete")
        print("5. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
