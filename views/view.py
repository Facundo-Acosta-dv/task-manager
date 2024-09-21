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

    # TO-DO MENU HEADERS AND OPTIONS PRINT SEPARATELY.
    def main_menu_header(self, header_text=""):
        if header_text: # If a header is given, prints it.
            header_text += "\n"
        return (f"Main menu\n{header_text}1.Add user - 2.Load user - 3.List users")


    # Displays main menu on terminal.
    def main_menu(self):
        terminal.clear_console()
        # Main menu options variables.
        min_options = 1
        max_options = 4
        out_of_range_text = ""
        value_error_text = ""
        prompt_text = f"What do you wanna do?: "
        
        debug_log(controller.menu_input(min_options, max_options, prompt_text, out_of_range_text, value_error_text))
        
            
    

            