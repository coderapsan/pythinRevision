# 




# Final Main.py 

from task_lists import TaskList
from task_lists import Task
import datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks.

    Args:
        task_list (TaskList): Task list to propagate.

    Returns:
        TaskList: The propagated task list.
    """
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list


def main():
    task_list = TaskList("Apsan")
    task_list = propagate_task_list(task_list)

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
            try:
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)
            except ValueError:
                print("Invalid date format.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            task_list.view_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            if 0 <= index < len(task_list.tasks):
                task_list.tasks[index].mark_completed()
            else:
                print("Invalid index.")

        elif choice == "4":
            task_list.view_tasks()
            index = int(input("Enter task number to edit: ")) - 1
            if 0 <= index < len(task_list.tasks):
                task = task_list.tasks[index]
                print("\nEdit Options:")
                print("a. Change title")
                print("b. Change due date")
                print("c. Both")
                edit_choice = input("Select option (a/b/c): ")

                if edit_choice == "a" or edit_choice == "c":
                    new_title = input("Enter new title: ")
                    task.change_title(new_title)

                if edit_choice == "b" or edit_choice == "c":
                    new_due = input("Enter new due date (YYYY-MM-DD): ")
                    try:
                        new_due_date = datetime.datetime.strptime(new_due, "%Y-%m-%d")
                        task.change_date_due(new_due_date)
                    except ValueError:
                        print("Invalid date format.")
            else:
                print("Invalid index.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()





