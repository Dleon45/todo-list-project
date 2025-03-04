tasks = []

def display_menu():
    """Display the main menu for the application."""
    print("\n--- TO-DO List ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Quit")


def add_task():
    """Add a task to the list."""
    task = input("Enter the task to add: ")
    if task.strip() == "":
        print("Task cannot be empty.")
    else:
        task.append(task)
        print(f"Task '{task}' has been added. ")
 
 
def view_tasks():
    """Display all task. """
    if not tasks:
        print("There are no tasks to view.")
    else:
        print("\n-- Current Task --")
        for index, task in enumerate(tasks,1):
            print(f"{index}. {task}")

def delete_task():
    """Delete a task from the list."""
    if not tasks:
        print("there are no tasks to delete.")
        return
    
    try:
        task_number = int(input("Enter the task number to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
        else:
            remove_task = tasks.pop(task_number - 1)
            print(f"Task '{remove_task}' has been deleted.")
    except ValueError:
        print("Please enter a valid number.")
        
def main():
    """Main function to interact with the user and run the program."""
    print("Welcome to your TO-DO list ")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Please choose an option (1-4):"))
            
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Goodbye! Thank you for using the TO-DO list.")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        print()

if __name__ == "__main__":
    main()
        
