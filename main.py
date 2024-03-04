tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}: {task}")

def deleteTask():
    if not tasks:
        print("There are no tasks to delete.")
        return
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task you want to delete: "))
        if taskToDelete <= len(tasks) and taskToDelete >= 0:
            tasks.pop(taskToDelete-1)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task {taskToDelete} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("Welcome to the to do list app :)")
    while True:
        print("\nPlease select one of the following options")
        print("============================================")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again")

    print("Goodbye 👋👋")