# import datetime

# class Task:
#     def __init__(self, title: str, date_due: datetime.datetime):
#         self.title: str = title
#         self.date_due: datetime.datetime = date_due
#         self.completed: bool = False

#     def mark_complete(self) -> None:
#         self.completed = True

#     def __str__(self) -> str:
#         return f"{self.title} - Due: {self.date_due.strftime('%Y-%m-%d')} - Completed: {self.completed}"



#Docstrings and comments 
# import datetime

# class Task:
#     """Represents a task in a to-do list application."""

#     def __init__(self, title: str, date_due: datetime.datetime):
#         self.title: str = title
#         self.date_due: datetime.datetime = date_due
#         self.completed: bool = False

#     def mark_complete(self) -> None:
#         """Marks the task as completed."""
#         self.completed = True

#     def __str__(self) -> str:
#         return f"{self.title} - Due: {self.date_due.strftime('%Y-%m-%d')} - Completed: {self.completed}"



#Portfolio 1 ::


import datetime

class Task:
    """Represents a task in a to-do list application."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str = ""):
        self.title: str = title
        self.date_due: datetime.datetime = date_due
        self.completed: bool = False
        self.description: str = description

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_description(self, new_description: str) -> None:
        """Changes the description of the task.
        
        Args:
            new_description: The new description for the task
        """
        self.description = new_description

    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        desc = f"\n   Description: {self.description}" if self.description else ""
        return (f"{self.title} - Due: {self.date_due.strftime('%Y-%m-%d')} "
                f"[{status}]{desc}")