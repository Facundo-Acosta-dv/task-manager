# task_manager.py

from models.task import Task
from controllers.controllers import Controller
from controllers.user_manager import UserManager

controller = Controller()
user_manager = UserManager()

class TaskManager:

    # Initializes the constructor.
    def __init__(self):
        pass

    # Starts the process of creating a task.
    def create_task(self, user_id):
        if user_manager.user_exists(user_id): # Verifies if the ID given matchs with an user one.
            # Logic for adding a task.
            controller.debug_log("Executing create_task()...")
            task_title = str(input("Task title: "))
            task_description = str(input("Task description: "))
            time_created = controller.get_time()
            date_created = controller.get_date()
            task = Task(time_created, date_created, task_title, task_description)
            self.save_task(user_id, task)
            # TO-DO Checks if the user has the task added and returns a success message.
            print(f"Task {task_title} added successfully! ")
        else: # Prints "User not found! " if "user_exists(user_id)" returns False.
            print("User not found! ")

    # Saves the user file with the task given and saves it to "users.json".
    def save_task(self, user_id, task):
        users = user_manager.load_users()
        for index, user in enumerate(users):
            if user.get("id") == str(user_id):
                users[index].get("tasks").append(task.__dict__)
                user_manager.save_users(users)
                controller.debug_log(users)
        