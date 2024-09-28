# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "status": "pending"})
    print(f'Task "{task}" added.')

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = task["status"]
            print(f"{index}. {task['task']} - {status}")

# Function to remove a task by index
def remove_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f'Task "{removed_task["task"]}" removed.')
    except IndexError:
        print("Invalid index. Please try again.")

# Optional: Function to mark a task as completed
def mark_task_completed(index):
    try:
        tasks[index - 1]["status"] = "completed"
        print(f'Task "{tasks[index - 1]["task"]}" marked as completed.')
    except IndexError:
        print("Invalid index")

# Main loop to keep the program running
#taken as choice for tasks
while True:
    print("\nTo-Do List Application")
    print("1. Add Task To-Do")
    print("2. Display Tasks")
    print("3. Remove Task")
    print("4. Mark the Task as Completed")
    print("5. Exit the application")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        index = int(input("Enter the task number to remove: "))
        remove_task(index)
    elif choice == "4":
        index = int(input("Enter the task number to mark as completed: "))
        mark_task_completed(index)
    elif choice == "5":
        print("Exiting the To-Do application. thankyou!")
        break
    else:
        print("Invalid choice. Please try again.")
