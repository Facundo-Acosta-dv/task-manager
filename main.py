# main.py

from controllers.controllers import Controller
from controllers.user_manager import UserManager
from controllers.task_manager import TaskManager
from controllers.menu import Menu
from views.terminal import Terminal
from views.view import View
import config

user_manager = UserManager()
task_manager = TaskManager()
terminal = Terminal()
view = View()
controller = Controller()
menu = Menu()
config.DEBUG = True # DELETE THIS AFTER FINISH SCRIPT.

def main(): # WARNING: i'm just using "main()" for testing purposes and debugging atm, thanks for your understanding!
    
    # TO-DO Rewrite task system
    # user_id = "6fa12d75-614e-4524-890a-0ec7cab4a826"
    # task_manager.create_task(user_id)
    while True:
        menu.main_menu() #REFactorise main_menu int func.
    # controller.int_in_range(1,5)
    # Creating an user
    # controller.validate_int_range(1, 3)
    # if controller.yes_or_no('Do you wish to create an user?: '): user_manager.create_user()

    #task_manager.add_task()
    #user_manager.save_user(test_user)
    #user_manager.load_user("1")
    #user_manager.info_user('1')
    
    
if __name__ == "__main__":
    main()