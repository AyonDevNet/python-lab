# Simple CLI To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ADD TASK
    if choice == "1":
        title = input("Enter task title: ")
        task = {"title": title, "done": False}
        tasks.append(task)
        print(" Task added successfully")

    # VIEW TASKS
    elif choice == "2":
        if len(tasks) == 0:
            print(" No tasks found")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Pending"
                print(f"{index + 1}. {task['title']} [{status}]")

    # MARK TASK AS DONE
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update")
        else:
            task_no = int(input("Enter task number to mark as done: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["done"] = True
                print("Task marked as done")
            else:
                print("Invalid task number")

    # DELETE TASK
    elif choice == "4":
        if len(tasks) == 0:
            print(" No tasks to delete")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted = tasks.pop(task_no - 1)
                print(f" Deleted task: {deleted['title']}")
            else:
                print(" Invalid task number")

    # EXIT
    elif choice == "5":
        print(" Exiting To-Do List. Goodbye!")
        break

    # INVALID INPUT
    else:
        print(" Invalid choice. Please select 1-5.")
