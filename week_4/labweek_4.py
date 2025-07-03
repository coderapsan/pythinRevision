#Task 1: Creating a Class TaskList and adding different methods 

#---------------------------------------------------------------
# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner.upper()
#         self.tasks = ["Write", "Read", "Do Homework", "Play"]

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, ix):
#         if 0 <= ix < len(self.tasks):
#             del self.tasks[ix]
#         else:
#             print("Invalid index.")

# #Using the above task for sample 
# my_tasks = TaskList("MaheshProgramming")
# print("Before removing:", my_tasks.tasks)
# #View task as per the question 
# my_tasks.remove_task(1)
# print("After removing:", my_tasks.tasks)


# ============================================================

#Task2 : Using enum to display the tasks with all their respective indexes 
#-----------------------------------------------------------

# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner.upper()
#         self.tasks = ["Write", "Read", "Do Homework", "Play"]

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, ix):
#         if 0 <= ix < len(self.tasks):
#             del self.tasks[ix]
#         else:
#             print("Invalid index.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks available.")
#         else:
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")



#----------------------------------------------------------

#Exercise 3 : Tesing the code with functionality 

#-----------------------------------------------------


# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner.upper()
#         self.tasks = ["Write", "Read", "Do Homework", "Play"]

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, ix):
#         if 0 <= ix < len(self.tasks):
#             del self.tasks[ix]
#         else:
#             print("Invalid index.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks available.")
#         else:
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")

# # using above methods to demonstrate the usage   ---------------> This is the appended code for task 3 demonstration part 
# my_tasks = TaskList("MaheshProgramming")
# my_tasks.view_tasks()




#---------------------------------------------------------------------
# Define the Task class as per the exercise

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False  # New attribute as per updated UML

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{status} Task: {self.title}"


#-----------------------------------------------------------
# Define the TaskList class to manage multiple Task objects

# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner.upper()
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, ix):
#         if 0 <= ix < len(self.tasks):
#             del self.tasks[ix]
#         else:
#             print("Invalid index.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks available to view.")
#         else:
#             print(f"\n{self.owner}'s Task List:")
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")

#     def list_options(self):
#         while True:
#             print("\nOptions:")
#             print("1: Add Task")
#             print("2: View Tasks")
#             print("3: Remove Task")
#             print("4: Mark Task as Completed")
#             print("5: Change Task Title")
#             print("6: Quit")

#             choice = input("Choose an option: ")
#             if choice == "1":
#                 title = input("Enter a task: ")
#                 task = Task(title)
#                 self.add_task(task)
#             elif choice == "2":
#                 self.view_tasks()
#             elif choice == "3":
#                 self.view_tasks()
#                 ix = int(input("Enter the index to remove: "))
#                 self.remove_task(ix)
#             elif choice == "4":
#                 self.view_tasks()
#                 ix = int(input("Enter index to mark as completed: "))
#                 if 0 <= ix < len(self.tasks):
#                     self.tasks[ix].mark_completed()
#                 else:
#                     print("Invalid index.")
#             elif choice == "5":
#                 self.view_tasks()
#                 ix = int(input("Enter index to change title: "))
#                 if 0 <= ix < len(self.tasks):
#                     new_title = input("Enter new title: ")
#                     self.tasks[ix].change_title(new_title)
#                 else:
#                     print("Invalid index.")
#             elif choice == "6":
#                 print("Goodbye!")
#                 break
#             else:
#                 print("Invalid choice.")


#--------------------------------------------------------------------------
# Test the application

# if __name__ == "__main__":
#     my_task_list = TaskList("MaheshProgramming")

#     # Add some initial tasks
#     my_task_list.tasks = [
#         Task("Do Homework"),
#         Task("Do Laundry"),
#         Task("Go Shopping")
#     ]

#     # Demo changes before menu
#     my_task_list.tasks[0].mark_completed()
#     my_task_list.tasks[1].change_title("Wash Clothes")

#     # Run the menu
#     my_task_list.list_options()
    
    #-------------------------------------------------------------------------
    
    #Adding completed attribute to the init  
    
    #----------------------------------------------
    
    
    # class Task:
    #   def __init__(self, title):
    #     self.title = title
    #     self.completed = False  # initially set to False as per the task 

    # def mark_completed(self):
    #     self.completed = True  # When function is called it will changed to true 

    # def change_title(self, new_title):
    #     self.title = new_title  # update the task title

    # def __str__(self):
    #     status = "Completed" if self.completed else "Incomplete"
    #     return f"{status} Task: {self.title}"




#---------------------------------------------------------------------

#Testing all the code functionalities of above code 

#------------------------------------------------------

# if __name__ == "__main__":
#     # Create a task
#     task1 = Task("Buy groceries")
#     print(task1)  # Expected:  Incomplete Task: Buy groceries

#     # Mark as completed
#     task1.mark_completed()
#     print(task1) 

#     # Change the title
#     task1.change_title("Buy fresh fruits")
#     print(task1)  




#-------------------------------------------------------------


#Modified List Options Method 


# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner
#         self.tasks = []

#     def add_task(self, task_title):
#         new_task = Task(task_title)
#         self.tasks.append(new_task)

#     def list_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#         else:
#             for i, task in enumerate(self.tasks):
#                 print(f"{i + 1}. {task}")

#     def list_options(self):
#         while True:
#             print("\nTask List Menu")
#             print("1. View tasks")
#             print("2. Add a task")
#             print("3. Mark a task as completed")
#             print("4. Change the title of a task")
#             print("5. Exit")

#             choice = input("Choose an option: ")

#             if choice == "1":
#                 self.list_tasks()

#             elif choice == "2":
#                 title = input("Enter the title of the new task: ")
#                 self.add_task(title)
#                 print("Task added.")

#             elif choice == "3":
#                 self.list_tasks()
#                 index = int(input("Enter the number of the task to mark as completed: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     self.tasks[index].mark_completed()
#                     print("Task marked as completed.")
#                 else:
#                     print("Invalid task number.")

#             elif choice == "4":
#                 self.list_tasks()
#                 index = int(input("Enter the number of the task to change the title: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     new_title = input("Enter the new title: ")
#                     self.tasks[index].change_title(new_title)
#                     print("Task title updated.")
#                 else:
#                     print("Invalid task number.")

#             elif choice == "5":
#                 print("Exiting Task List.")
#                 break

#             else:
#                 print("Invalid option. Please try again.")



#Python Libraries 

#Adding more functionalities like date created and due date to each 

import datetime  #imprting datetime library

#Lets update the task class first 

class Task:
    def __init__(self, title, date_due):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title):
        self.title = new_title

    def change_date_due(self, date_due):
        self.date_due = date_due

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return (f"{self.title} [{status}] | "
                f"Created: {self.date_created.strftime('%Y-%m-%d')} | "
                f"Due: {self.date_due.strftime('%Y-%m-%d')}")



#Lets update the TaskList Class to us the latest feature that we implemented on Task class Structure 

# class TaskList:
#     def __init__(self, owner):
#         self.owner = owner
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def list_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#         else:
#             for i, task in enumerate(self.tasks):
#                 print(f"{i + 1}. {task}")

#     def list_options(self):
#         while True:
#             print("\nTask List Menu")
#             print("1. Add a task")
#             print("2. View tasks")
#             print("3. Mark a task as completed")
#             print("4. Change the title of a task")
#             print("5. Change due date of a task")
#             print("6. Exit")

#             choice = input("Choose an option: ")

#             if choice == "1":
#                 title = input("Enter a task title: ")
#                 input_date = input("Enter a due date (YYYY-MM-DD): ")
#                 try:
#                     date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
#                     task = Task(title, date_object)
#                     self.add_task(task)
#                     print("Task added.")
#                 except ValueError:
#                     print("Invalid date format. Please use YYYY-MM-DD.")

#             elif choice == "2":
#                 self.list_tasks()

#             elif choice == "3":
#                 self.list_tasks()
#                 index = int(input("Enter task number to mark as completed: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     self.tasks[index].mark_completed()
#                     print("Task marked as completed.")
#                 else:
#                     print("Invalid task number.")

#             elif choice == "4":
#                 self.list_tasks()
#                 index = int(input("Enter task number to change the title: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     new_title = input("Enter new title: ")
#                     self.tasks[index].change_title(new_title)
#                     print("Task title updated.")
#                 else:
#                     print("Invalid task number.")

#             elif choice == "5":
#                 self.list_tasks()
#                 index = int(input("Enter task number to change due date: ")) - 1
#                 if 0 <= index < len(self.tasks):
#                     new_due = input("Enter new due date (YYYY-MM-DD): ")
#                     try:
#                         new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
#                         self.tasks[index].change_date_due(new_due_date)
#                         print("Due date updated.")
#                     except ValueError:
#                         print("Invalid date format.")
#                 else:
#                     print("Invalid task number.")

#             elif choice == "6":
#                 print("Exiting Task List.")
#                 break

#             else:
#                 print("Invalid option.")
#  #Lets Check the above examples 
 
# if __name__ == "__main__":
#     my_tasks = TaskList("MaheshProgramming")
#     my_tasks.list_options()



#Change Title and Due Date 
#---------------------------------------------------

def list_options(self):
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Edit a task")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            task = Task(title, date_object)
            self.add_task(task)

        elif choice == "2":
            self.view_tasks()

        elif choice == "3":
            self.view_tasks()
            index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].mark_completed()

        elif choice == "4":
            self.view_tasks()
            index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= index < len(self.tasks):
                task = self.tasks[index]
                print("\nEdit Options:")
                print("a. Change title")
                print("b. Change due date")
                print("c. Both")

                edit_choice = input("What would you like to edit? (a/b/c): ")

                if edit_choice == "a" or edit_choice == "c":
                    new_title = input("Enter new title: ")
                    task.change_title(new_title)

                if edit_choice == "b" or edit_choice == "c":
                    new_due = input("Enter new due date (YYYY-MM-DD): ")
                    new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                    task.change_date_due(new_due_date)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
            
            
# Les Confirrm we have parameter change_title and change due_date 
class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def list_options(self):
        while True:
            print("\nTask List Menu")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as completed")
            print("4. Change the title of a task")
            print("5. Change due date of a task")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter a task title: ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                try:
                    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                    task = Task(title, date_object)
                    self.add_task(task)
                    print("Task added.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif choice == "2":
                self.list_tasks()

            elif choice == "3":
                self.list_tasks()
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(self.tasks):
                    self.tasks[index].mark_completed()
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")

            elif choice == "4":
                self.list_tasks()
                index = int(input("Enter task number to change the title: ")) - 1
                if 0 <= index < len(self.tasks):
                    new_title = input("Enter new title: ")
                    self.tasks[index].change_title(new_title)
                    print("Task title updated.")
                else:
                    print("Invalid task number.")

            elif choice == "5":
                self.list_tasks()
                index = int(input("Enter task number to change due date: ")) - 1
                if 0 <= index < len(self.tasks):
                    new_due = input("Enter new due date (YYYY-MM-DD): ")
                    try:
                        new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                        self.tasks[index].change_date_due(new_due_date)
                        print("Due date updated.")
                    except ValueError:
                        print("Invalid date format.")
                else:
                    print("Invalid task number.")

            elif choice == "6":
                print("Exiting Task List.")
                break

            else:
                print("Invalid option.")
 #Lets Check the above examples 
 

def change_title(self, new_title):
    self.title = new_title

def change_date_due(self, new_due_date):
    self.date_due = new_due_date


if __name__ =="main":
    my_tasks = TaskList("MaheshP")
    my_tasks.list_options()




#-------------------------------------------------------------------------------------------------


