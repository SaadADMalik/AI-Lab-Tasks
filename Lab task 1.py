tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
