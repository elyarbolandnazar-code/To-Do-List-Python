import os

tasks = []

def show_menu():
        print("=====To_Do list=====")
        print("1.افزودن کار")
        print("2.نمایش کارها")
        print("3.خروج")
        print("4.حذف کار")
        print("5.ویرایش کار")
        print("6.علامت زدن کارهای انجام‌شده ")
        print("7.جستجوی کار")

def save_tasks():
        with open("tasks.txt", "w", encoding="utf-8") as file:
                for task in tasks:
                        file.write(f"{task[0]}|{task[1]}\n")

def get_priority():
    print("1.مهم🔴")
    print("2.عادي🟠")
    print("3.کم اهميت🟢")
    priority=input("اولويت کار را انتخاب کنيد: ")
    
    
    if priority in ["1","۱"]:
            priority_text="🔴"
    elif priority in ["2","۲"]:
            priority_text="🟠"
    elif priority in ["3","۳"]:
            priority_text="🟢"
    else:
            print("گزينه نامعتبر است.")
            return None
    return priority_text
                
def add_task():
    task = input("کار جدید را وارد کنید.")
    priority_text=get_priority()
    if priority_text is None:
            return
    tasks.append([task,priority_text])
    save_tasks()
    print("کار اضافه شد.")                  

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
    print("لیست کار ها:\n")
        
    if not tasks:
        print("هیچ کاری ثبت نشده است.")
            
    else:
        sorted_tasks = sorted(tasks, key=sort_by_priority)

        for i, task in enumerate(sorted_tasks, start=1):
            print(f"{i}. {task[0]}{task[1]}")


def get_number():
    try:
        number = int(input("شماره کار مورد نظر را وارد کنید: "))
    except ValueError:
        print("لطفا عدد وارد کنید.")
        return

    if 1 <= number <= len(tasks):
        return number
    else:
        print("شماره نامعتبر است.")
            
def delete_task():
    if not tasks:
        print("هیچ کاری برای حذف وجود ندارد.")
        return

    show_tasks()

    number = get_number()

    if number is None:
        return

    selected_task = sorted_tasks[number - 1]
    tasks.remove(selected_task)
    save_tasks()
    print("کار حذف شد.")
    show_tasks()
                
def edit_task():
    if not tasks:
        print("هیچ کاری برای ویرایش وجود ندارد.")
            
    else:
        show_tasks()
        sorted_tasks=sorted(tasks, key=sort_by_priority)
        number = get_number()
        
        if number is None:
                return

        
        
        new_task = input("متن جدید را وارد کنید:")
        priority=get_priority()
        if priority is None:
            return
        
        selected_task=sorted_tasks[number - 1]
        selected_task[0]=new_task
        selected_task[1]=priority
            
        save_tasks()
        print("کار با موفقیت ویرایش شد.")
        show_tasks()
        
                
def complete_task():
    if not tasks:
        print("هیچ کاری ثبت نشده است.")
    else:
        show_tasks()
        sorted_tasks=sorted(tasks, key=sort_by_priority)
        number = get_number()
        if number is None:
                return

        selected_task=sorted_tasks[number - 1]

        if selected_task[0].startswith("✔"):
            print("این کار قبلاً انجام شده است.")
        else:
            selected_task[0] = "✔ " + selected_task[0]
            save_tasks()
            print("کاربه عنوان انجام‌شده علامت‌گذاری شد.")
            show_tasks()

def search_task():
    if not tasks:
        print("هیچ کاری ثبت نشده است.")
        return

    search = input("کار مورد نظر را وارد کنید.")
    if not search:
            print("عبارت جستجو را وارد کنيد.")
            return
    found = False
    
    for i, task in enumerate(tasks, start = 1):
        if search.lower() in task[0].lower():
            print(f"{i}. {task[0]} {task[1]}")
            found = True

    if not found:
        print("کار مورد نظر پیدا نشد.")
            
load_tasks()

while True:
        show_menu()

        choice = input("انتخاب شما:")
        if choice in ["1", "۱"]:
                add_task()
                
        elif choice in ["2", "۲"]:
                show_tasks()
                                
        elif choice in ["3", "۳"]:
                print("خروج از برنامه.")
                break

        elif choice in ["4", "۴"]:
                delete_task()
                
        elif choice in ["5", "۵"]:
                edit_task()
                
        elif choice in ["6", "۶"]:
                complete_task()

        elif choice in ["7", "۷"]:
                search_task()

        else:
                print("گزینه نامعتبر است.")
