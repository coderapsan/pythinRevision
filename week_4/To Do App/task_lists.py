# import datetime

# class Task:
#     def __init__(self, title, date_due):
#         self.title = title
#         self.date_due = date_due
#         self.completed = False

#     def mark_completed(self):
#         self.completed = True

#     def change_title(self, new_title):
#         self.title = new_title

#     def change_date_due(self, new_due_date):
#         self.date_due = new_due_date

#     def __str__(self):
#         status = "✓" if self.completed else "✗"
#         return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d')}) - {status}"


# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks added yet.")
#             return
#         for idx, task in enumerate(self.tasks, 1):
#             print(f"{idx}. {task}")

#     def list_options(self):
#         while True:
#             print("\nOptions:")
#             print("1. Add a task")
#             print("2. View tasks")
#             print("3. Mark a task as completed")
#             print("4. Edit a task")
#             print("5. Quit")

#             choice = input("Choose an option: ")

#             if choice == "1":
#                 title = input("Enter a task: ")
#                 input_date = input("Enter a due date (YYYY-MM-DD): ")
#                 try:
#                     date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
#                     task = Task(title, date_object)
#                     self.add_task(task)
#                 except ValueError:
#                     print("Invalid date format.")

#             elif choice == "2":
#                 self.view_tasks()

#             elif choice == "3":
#                 self.view_tasks()
#                 index = int(input("Enter task number to mark as completed: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     self.tasks[index].mark_completed()

#             elif choice == "4":
#                 self.view_tasks()
#                 index = int(input("Enter task number to edit: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     task = self.tasks[index]
#                     print("\nEdit Options:")
#                     print("a. Change title")
#                     print("b. Change due date")
#                     print("c. Both")
#                     edit_choice = input("Select option (a/b/c): ")

#                     if edit_choice == "a" or edit_choice == "c":
#                         new_title = input("Enter new title: ")
#                         task.change_title(new_title)

#                     if edit_choice == "b" or edit_choice == "c":
#                         new_due = input("Enter new due date (YYYY-MM-DD): ")
#                         try:
#                             new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
#                             task.change_date_due(new_due_date)
#                         except ValueError:
#                             print("Invalid date format.")

#             elif choice == "5":
#                 break

#             else:
#                 print("Invalid choice. Try again.")









##### Final Task_lists.py 
# import datetime

# class Task:
#     def __init__(self, title, date_due):
#         self.title = title
#         self.date_due = date_due
#         self.completed = False

#     def mark_completed(self):
#         self.completed = True

#     def change_title(self, new_title):
#         self.title = new_title

#     def change_date_due(self, new_due_date):
#         self.date_due = new_due_date

#     def __str__(self):
#         status = "✓" if self.completed else "✗"
#         return f"{self.title} (Due: {self.date_due.strftime('%Y-%m-%d')}) - {status}"


# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks added yet.")
#             return
#         for idx, task in enumerate(self.tasks, 1):
#             print(f"{idx}. {task}")


#####################Type Checking 

# from typing import List
# from tasks import Task

# class TaskList:
#     def __init__(self):
#         self.tasks: List[Task] = []

#     def add_task(self, task: Task) -> None:
#         self.tasks.append(task)

#     def remove_task(self, index: int) -> None:
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]

#     def get_tasks(self) -> List[Task]:
#         return self.tasks

#     def get_task(self, index: int) -> Task:
#         return self.tasks[index]

#     def complete_task(self, index: int) -> None:
#         self.tasks[index].mark_complete()





#Docstrings and comments 


# from typing import List
# from tasks import Task

# class TaskList:
#     """A class to manage a collection of Task objects."""

#     def __init__(self):
#         self.tasks: List[Task] = []

#     def add_task(self, task: Task) -> None:
#         """Adds a task to the task list.

#         Args:
#             task (Task): The task to be added.
#         """
#         self.tasks.append(task)

#     def remove_task(self, index: int) -> None:
#         """Removes a task from the list by its index.

#         Args:
#             index (int): The index of the task to be removed.
#         """
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]

#     def get_tasks(self) -> List[Task]:
#         """Returns the list of all tasks.

#         Returns:
#             List[Task]: The current list of tasks.
#         """
#         return self.tasks

#     def get_task(self, index: int) -> Task:
#         """Retrieves a single task by index.

#         Args:
#             index (int): The index of the task to retrieve.

#         Returns:
#             Task: The task at the specified index.
#         """
#         return self.tasks[index]

#     def complete_task(self, index: int) -> None:
#         """Marks the task at the given index as complete.

#         Args:
#             index (int): The index of the task to mark complete.
#         """
#         self.tasks[index].mark_complete()






#Portfolio ::2

from typing import List
from tasks import Task
import datetime

class TaskList:
    """A class to manage a collection of Task objects."""

    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the task list."""
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        """Removes a task from the list by its index."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_tasks(self) -> List[Task]:
        """Returns the list of all tasks."""
        return self.tasks

    def get_task(self, index: int) -> Task:
        """Retrieves a single task by index."""
        return self.tasks[index]

    def complete_task(self, index: int) -> None:
        """Marks the task at the given index as complete."""
        self.tasks[index].mark_complete()

    def view_overdue_tasks(self) -> None:
        """Displays all tasks that are overdue (past due date and not completed)."""
        current_date = datetime.datetime.now()
        overdue_tasks = [
            task for task in self.tasks
            if task.date_due < current_date and not task.completed
        ]
        
        print("\nOverdue Tasks:")
        if not overdue_tasks:
            print("No overdue tasks.")
        for idx, task in enumerate(overdue_tasks):
            print(f"{idx}. {task}")