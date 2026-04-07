#Project
#Task_Schedular

from datetime import datetime

tasks = []

def add_task():
    name = input("Task name: ")
    due = input("Due date (YYYY-MM-DD HH:MM): ")
    try:
        due_date = datetime.strptime(due, "%Y-%m-%d %H:%M")
        tasks.append({"name": name, "due": due_date, "done": False})
        print("Task added.")
    except:
        print("Invalid date format.")

def show_pending(show_index=False):
    print("\nPending Tasks:")
    i = 1
    for task in sorted(tasks, key=lambda t: t["due"]):
        if not task["done"]:
            if show_index:
                print(f"{i}. {task['name']} - {task['due'].strftime('%Y-%m-%d %H:%M')}")
            else:
                print(f"- {task['name']}")
            i += 1
    if i == 1:
        print("No pending tasks.")

def complete_task():
    show_pending(show_index=True)
    try:
        idx = int(input("Enter task number to complete: ")) - 1
    except:
        print("Invalid input.")
        return

    count = -1
    for task in tasks:
        if not task["done"]:
            count += 1
            if count == idx:
                task["done"] = True
                print("Marked complete.")
                return
    print("Invalid task number.")

def show_completed():
    print("\nCompleted Tasks:")
    found = False
    for task in tasks:
        if task["done"]:
            print(f"- {task['name']}")
            found = True
    if not found:
        print("No completed tasks.")

# Main loop
while True:
    print("\n1.Add  2.Complete  3.Pending  4.Completed  5.Exit")
    ch = input("Choose: ")
    if ch == "1":
        add_task()
    elif ch == "2":
        complete_task()
    elif ch == "3":
        show_pending()
    elif ch == "4":
        show_completed()
    elif ch == "5":
        break
    else:
        print("Invalid choice.")
