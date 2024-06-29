def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        
        elif choice == '2':
            show_tasks(tasks)
        
        elif choice == '3':
            mark_task_done(tasks)
        
        elif choice == '4':
            print("Exiting the To-Do List.")
            break
        
        else:
            print("Invalid choice. Please try again.")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def show_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

def mark_task_done(tasks):
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    main()