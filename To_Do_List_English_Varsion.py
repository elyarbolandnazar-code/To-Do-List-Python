import os

tasks = []

def show_menu():
        print("=====To_Do List=====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Edit Task")
        print("5. Mark Task as Completed")
        print("6. Search Task")
        print("7. Exit")

def save_tasks():
        with open("tasks.txt", "w", encoding="utf-8") as file:
                for task in tasks:
                        file.write(f"{task[0]}|{task[1]}\n")

def get_priority():
    print("1. Important 🔴")
    print("2. Normal 🟠")
    print("3. Low Priority 🟢")
    priority=input("Select task priority: ")
    
    
    if priority == "1":
            priority_text="🔴"
    elif priority == "2":
            priority_text="🟠"
    elif priority == "3":
            priority_text="🟢"
    else:
            print("Invalid option.")
            return None
    return priority_text
                
def add_task():
    task = input("Enter a new task: ")
    priority_text=get_priority()
    if priority_text is None:
            return
    tasks.append([task,priority_text])
    save_tasks()
    print("Task added.")                  

def load_tasks():
        if os.path.exists("tasks.txt"):
                with open("tasks.txt", "r", encoding="utf-8") as file:
                        for line in file:
                                line = line.strip()
                                parts = line.split("|")
                                if len(parts)==2:
                                        tasks.append(parts)

def sort_by_priority(task):
    if task[1] == "🔴":
        return 1
    elif task[1] == "🟠":
        return 2
    elif task[1] == "🟢":
        return 3

def show_tasks():
    print("Task List:\n")
        
    if not tasks:
        print("No tasks have been added.")
            
    else:
        sorted_tasks = sorted(tasks, key=sort_by_priority)

        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task[0]}{task[1]}")


def get_number():
    try:
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a number.")
        return

    if 1 <= number <= len(tasks):
        return number
    else:
        print("Invalid number.")
            
def delete_task():
    if not tasks:
        print("There are no tasks to delete.")
        return

    show_tasks()
    sorted_tasks=sorted(tasks, key=sort_by_priority)
    number = get_number()

    if number is None:
        return

    selected_task = sorted_tasks[number - 1]
    tasks.remove(selected_task)
    save_tasks()
    print("Task deleted.")
    show_tasks()
                
def edit_task():
    if not tasks:
        print("There are no tasks to edit.")
            
    else:
        show_tasks()
        sorted_tasks=sorted(tasks, key=sort_by_priority)
        number = get_number()
        
        if number is None:
                return

        
        
        new_task = input("Enter the new task text:")
        priority=get_priority()
        if priority is None:
            return
        
        selected_task=sorted_tasks[number - 1]
        selected_task[0]=new_task
        selected_task[1]=priority
            
        save_tasks()
        print("Task edited successfully.")
        show_tasks()
        
                
def complete_task():
    if not tasks:
        print("No tasks have been added.")
    else:
        show_tasks()
        sorted_tasks=sorted(tasks, key=sort_by_priority)
        number = get_number()
        if number is None:
                return

        selected_task=sorted_tasks[number - 1]

        if selected_task[0].startswith("✔"):
            print("This task is already completed.")
        else:
            selected_task[0] = "✔ " + selected_task[0]
            save_tasks()
            print("Task marked as completed.")
            show_tasks()

def search_task():
    if not tasks:
        print("No tasks have been added.")
        return

    search = input("Enter the task to search for: ")
    if not search:
            print("Please enter a search term.")
            return
    found = False
    
    for i, task in enumerate(tasks, start = 1):
        if search.lower() in task[0].lower():
            print(f"{i}. {task[0]} {task[1]}")
            found = True

    if not found:
        print("Task not found.")
            
load_tasks()

while True:
        show_menu()

        choice = int(input("Your choice:"))
        if choice == "1":
                add_task()
                
        elif choice == "2":
                show_tasks()
                                
        elif choice == "3":
                delete_task()   

        elif choice == "4":
                edit_task()
                
        elif choice == "5":
                complete_task()

        elif choice == "6":
                search_task()
                
        elif choice == "7":
                print("Exiting the program.")
                break                

        else:
                print("Invalid option.")
