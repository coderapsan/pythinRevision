# 




# Final Main.py 

# from task_lists import TaskList
# from task_lists import Task
# import datetime

# def propagate_task_list(task_list: TaskList) -> TaskList:
#     """Propagates a task list with some sample tasks.

#     Args:
#         task_list (TaskList): Task list to propagate.

#     Returns:
#         TaskList: The propagated task list.
#     """
#     task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
#     task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
#     task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
#     task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
#     task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
#     task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
#     return task_list


# def main():
#     task_list = TaskList("Apsan")
#     task_list = propagate_task_list(task_list)

#     while True:
#         print("\nOptions:")
#         print("1. Add a task")
#         print("2. View tasks")
#         print("3. Mark a task as completed")
#         print("4. Edit a task")
#         print("5. Quit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             title = input("Enter a task: ")
#             input_date = input("Enter a due date (YYYY-MM-DD): ")
#             try:
#                 date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
#                 task = Task(title, date_object)
#                 task_list.add_task(task)
#             except ValueError:
#                 print("Invalid date format.")

#         elif choice == "2":
#             task_list.view_tasks()

#         elif choice == "3":
#             task_list.view_tasks()
#             index = int(input("Enter task number to mark as completed: ")) - 1
#             if 0 <= index < len(task_list.tasks):
#                 task_list.tasks[index].mark_completed()
#             else:
#                 print("Invalid index.")

#         elif choice == "4":
#             task_list.view_tasks()
#             index = int(input("Enter task number to edit: ")) - 1
#             if 0 <= index < len(task_list.tasks):
#                 task = task_list.tasks[index]
#                 print("\nEdit Options:")
#                 print("a. Change title")
#                 print("b. Change due date")
#                 print("c. Both")
#                 edit_choice = input("Select option (a/b/c): ")

#                 if edit_choice == "a" or edit_choice == "c":
#                     new_title = input("Enter new title: ")
#                     task.change_title(new_title)

#                 if edit_choice == "b" or edit_choice == "c":
#                     new_due = input("Enter new due date (YYYY-MM-DD): ")
#                     try:
#                         new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
#                         task.change_date_due(new_due_date)
#                     except ValueError:
#                         print("Invalid date format.")
#             else:
#                 print("Invalid index.")

#         elif choice == "5":
#             break

#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()



#Type Checking 

# from typing import NoReturn
# from task_lists import TaskList
# from tasks import Task
# import datetime

# def propagate_task_list(task_list: TaskList) -> TaskList:
#     task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
#     task_list.add_task(Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)))
#     task_list.add_task(Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)))
#     task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
#     task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
#     task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
#     return task_list

# def main() -> NoReturn:
#     task_list: TaskList = TaskList()

#     # propagate the task list with some sample tasks
#     task_list = propagate_task_list(task_list)

#     while True:
#         print("\nToDo List Options:")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Mark Task as Complete")
#         print("4. Show Tasks")
#         print("5. Quit")

#         choice: str = input("Enter your choice: ")

#         if choice == "1":
#             title: str = input("Enter task title: ")
#             due_date_str: str = input("Enter due date (YYYY-MM-DD): ")
#             try:
#                 due_date: datetime.datetime = datetime.datetime.strptime(due_date_str, "%Y-%m-%d")
#                 task: Task = Task(title, due_date)
#                 task_list.add_task(task)
#                 print("Task added!")
#             except ValueError:
#                 print("Invalid date format. Please use YYYY-MM-DD.")
#         elif choice == "2":
#             index: int = int(input("Enter index of task to remove: "))
#             task_list.remove_task(index)
#         elif choice == "3":
#             index: int = int(input("Enter index of task to mark complete: "))
#             task_list.complete_task(index)
#         elif choice == "4":
#             print("\nCurrent Tasks:")
#             for idx, task in enumerate(task_list.get_tasks()):
#                 print(f"{idx}. {task}")
#         elif choice == "5":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()




#Docstrings and comments 
from typing import NoReturn
from task_lists import TaskList
from tasks import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Prepopulates the task list with sample tasks for demonstration.
    
    Args:
        task_list: The TaskList instance to populate with sample tasks
        
    Returns:
        The populated TaskList instance with sample tasks
    """
    sample_tasks = [
        ("Buy groceries", -4),  # 4 days ago
        ("Do laundry", 2),      # in 2 days
        ("Clean room", -1),      # yesterday
        ("Do homework", 3),      # in 3 days
        ("Walk dog", 5),        # in 5 days
        ("Do dishes", 6)        # in 6 days
    ]
    
    for title, days in sample_tasks:
        due_date = datetime.datetime.now() + datetime.timedelta(days=days)
        task_list.add_task(Task(title, due_date))
    
    return task_list

def get_valid_date_input(prompt: str) -> datetime.datetime:
    """Helper function to get and validate date input from user.
    
    Args:
        prompt: The input prompt to display
        
    Returns:
        Validated datetime object
        
    Raises:
        ValueError: If input cannot be parsed as date
    """
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_int_input(prompt: str, max_val: int) -> int:
    """Helper function to get and validate integer input from user.
    
    Args:
        prompt: The input prompt to display
        max_val: Maximum acceptable value
        
    Returns:
        Validated integer within range
        
    Raises:
        ValueError: If input cannot be parsed as integer or is out of range
    """
    while True:
        try:
            val = int(input(prompt))
            if 0 <= val < max_val:
                return val
            print(f"Please enter a number between 0 and {max_val-1}")
        except ValueError:
            print("Please enter a valid number.")

def main() -> NoReturn:
    """Main entry point for the To-Do List application."""
    task_list = TaskList()
    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. View All Tasks")
        print("5. Edit Task")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":  # Add Task
            title = input("Enter task title: ")
            due_date = get_valid_date_input("Enter due date (YYYY-MM-DD): ")
            task_list.add_task(Task(title, due_date))
            print("Task added successfully!")

        elif choice == "2":  # Remove Task
            if not task_list.get_tasks():
                print("No tasks available to remove.")
                continue
                
            print("\nCurrent Tasks:")
            for idx, task in enumerate(task_list.get_tasks()):
                print(f"{idx}. {task}")
                
            task_idx = get_valid_int_input(
                "Enter task number to remove: ",
                len(task_list.get_tasks())
            )
            task_list.remove_task(task_idx)
            print("Task removed successfully!")

        elif choice == "3":  # Mark Complete
            if not task_list.get_tasks():
                print("No tasks available to mark complete.")
                continue
                
            print("\nCurrent Tasks:")
            for idx, task in enumerate(task_list.get_tasks()):
                print(f"{idx}. {task}")
                
            task_idx = get_valid_int_input(
                "Enter task number to mark complete: ",
                len(task_list.get_tasks())
            )
            task_list.complete_task(task_idx)
            print("Task marked as complete!")

        elif choice == "4":  # View Tasks
            print("\nCurrent Tasks:")
            if not task_list.get_tasks():
                print("No tasks available.")
            for idx, task in enumerate(task_list.get_tasks()):
                print(f"{idx}. {task}")

        elif choice == "5":  # Edit Task
            if not task_list.get_tasks():
                print("No tasks available to edit.")
                continue
                
            print("\nCurrent Tasks:")
            for idx, task in enumerate(task_list.get_tasks()):
                print(f"{idx}. {task}")
                
            task_idx = get_valid_int_input(
                "Enter task number to edit: ",
                len(task_list.get_tasks())
            )
            task = task_list.get_task(task_idx)
            
            print("\nEdit Options:")
            print("1. Change title")
            print("2. Change due date")
            print("3. Both title and due date")
            
            edit_choice = input("Select option (1-3): ")
            
            if edit_choice in ("1", "3"):
                new_title = input("Enter new title: ")
                task.title = new_title
                
            if edit_choice in ("2", "3"):
                new_due = get_valid_date_input("Enter new due date (YYYY-MM-DD): ")
                task.date_due = new_due
                
            print("Task updated successfully!")

        elif choice == "6":  # Quit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()