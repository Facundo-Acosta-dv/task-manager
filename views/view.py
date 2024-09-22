from controllers.controllers import Controller
from controllers.user_manager import UserManager
from utils import debug_log
from views.terminal import Terminal
import os, json

manager = UserManager()
controller = Controller()
terminal = Terminal()
author = "hi7nn"

class View:

    # I may deprecate this.
    def show_person(self, user):
        if user in manager.users:
            print(f"The user username is {user.username}")
        else:
            print("The user doesn't exist")
    
    # This too.
    def user_list(self):
        print(manager.users)
        for user in manager.users:
            print(user.age)

    # This too, too.
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