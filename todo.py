tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def mark_task_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
    else:
        print("Invalid task index.")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else " "
        print(f"{i + 1}. [{status}] {task['task']}")


def main():
    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")
        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            task = input('Enter the task')
            add_task(task)
            print("Task added successfully!")
        
        elif choice == '2':
            view_tasks()
            task_index = int(input('Enter the task number to mark as completed: ')) - 1
            mark_task_completed(task_index)
            print('Task marked as completed!')
        
        elif choice == '3':
            view_tasks()
        
        elif choice == '4':
            print('Exiting the ToDo list app.')
            break
        
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()