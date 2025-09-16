import json, os

FILE = "tasks.json"

def load_tasks():
    """
    Loads tasks from the tasks.json file.

    Returns a list of tasks, where each task is a dictionary containing the task name and a boolean indicating whether the task is done.

    If the tasks.json file does not exist, returns an empty list.
    """
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save_tasks(tasks):
    """
    Saves the given tasks to the tasks.json file.

    :param tasks: A list of tasks, where each task is a dictionary containing the task name and a boolean indicating whether the task is done.
    """
    json.dump(tasks, open(FILE, "w"), indent=2)

def add_task(task):
    """
    Adds a task to the tasks list.

    :param task: The task to add.
    """
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def list_tasks():
    """
    Prints all tasks in the tasks list.

    Each task is printed with a number, the task name, and a status indicator: "✔" if the task is done, or "✘" if the task is not done.
    """
    for i, t in enumerate(load_tasks(), 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(idx):
    """
    Marks the task at the given index as done.

    :param idx: The index of the task to mark as done.
    """
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)

def delete_task(idx):
    """
    Deletes the task at the given index.

    :param idx: The index of the task to delete.

    If the index is valid, the task is removed from the tasks list and the changes are saved to the tasks.json file.
    """
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)

def main():
    """
    Main loop of the todo list app.

    Prints the main menu and processes the user's choice.

    The main menu consists of the following options:
    1. Add task
    2. List tasks
    3. Mark task as done
    4. Delete task
    5. Quit

    The app will keep running until the user chooses to quit.
    """
    
    while True:
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            idx = int(input("Enter task number: "))
            mark_done(idx - 1)
        elif choice == "4":
            idx = int(input("Enter task number: "))
            delete_task(idx - 1)
        elif choice == "5":
            break   
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
