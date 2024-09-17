from models.user import User
from controllers.user_manager import UserManager
import os, json

manager = UserManager()
author = "hi7nn"

class TaskView:

    # TO-DO fix this fucking shit
    def show_person(self, user):
        if user in manager.users:
            print(f"The user username is {user.username}")
        else:
            print("The user doesn't exist")
    
    # List of all persons
    def user_list(self):
        print(manager.users)
        for user in manager.users:
            print(user.age)

    def display_user_info(self, user_id):
        filename = f'user_{user_id}_data.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                file = json.load(file)
                for key, value in file.items():
                    if key.lower() == 'tasks' and value == []:
                        print("• No tasks found!")
                    else:
                        print(f"• {key.capitalize()}: {value}")
            