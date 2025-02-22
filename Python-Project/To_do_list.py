# Load Existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items

import json

file_name = "To_Do.json"

def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_task(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to Save.")
    

def view_task(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("your task To-do list")
        for idx, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")

def create_task(tasks):
    description = input("Enter the task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_task(tasks)
        print("Task Added successfully.")
    else:
        print("description canyt be empty")


def main():
    tasks = load_task()
    print(tasks)

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Thats Enough")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
