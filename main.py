# main.py

from controllers.controllers import Controller
from controllers.user_manager import UserManager
from controllers.task_manager import TaskManager
from views.terminal import Terminal
from views.view import TaskView
import config

user_manager = UserManager()
task_manager = TaskManager()
terminal = Terminal()
view = TaskView()
controller = Controller()
config.DEBUG = True

def main(): # WARNING: i'm just using "main()" for testing purposes and debugging atm, thanks for your understanding!
    
    # TO-DO Rewrite task system
    user_id = "f716070d-c265-4c31-86d4-72d61a31477f"
    task_manager.create_task(user_id)
    # view.display_user_info(1)
    # user_manager.load_users()

    # Creating an user
    # if controller.yes_or_no('Do you wish to create an user?: '): user_manager.create_user()

    #task_manager.add_task()
    #user_manager.save_user(test_user)
    #user_manager.load_user("1")
    #user_manager.info_user('1')
    
    
if __name__ == "__main__":
    main()