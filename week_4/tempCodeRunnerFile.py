my_task_list = TaskList("Apsan")
my_task_list.tasks = [Task("Do Homework"), Task("Do Laundry"), Task("Go Shopping")]

# Optional: Mark a task as completed and change a title for demo
my_task_list.tasks[0].mark_completed()
my_task_list.tasks[1].change_title("Wash Clothes")

# Run the menu
my_task_list.list_options()