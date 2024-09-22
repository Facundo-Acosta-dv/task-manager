# menu.py
from views.terminal import Terminal
from controllers.controllers import Controller
from controllers.user_manager import UserManager
from utils import debug_log
terminal = Terminal()
controller = Controller()
user_manager = UserManager()

class Menu:

    # Displays main menu on terminal.
    def main_menu(self):
        terminal.clear_console()
        # Main menu options variables.
        min_options = 1
        max_options = 4
        out_of_range_text = ""
        value_error_text = ""
        prompt_text = f"What do you wanna do?: "
        
        user_input = self.menu_options(min_options, max_options, prompt_text, out_of_range_text, value_error_text)
        self.menu_input(user_input)
    
    # TO-DO MENU HEADERS AND OPTIONS PRINT SEPARATELY.
    def main_menu_header(self, header_text=""):
        if header_text: # Prints header if given.
            header_text += "\n"
        return (f"Main menu\n{header_text}1.Add user - 2.Load user - 3.List users - 4.Quit")
    
    # Gives the menu options and returns a number based on input.
    def menu_options(self, min, max, prompt_text="prompt_text_input_val", out_of_range_text="out of range", value_error_text="please, enter a valid number"):
        header = self.main_menu_header()
        return controller.int_in_range(min, max, prompt_text, out_of_range_text, value_error_text, True, header)
    
    def menu_input(self, option):
        try:
            match option: 
                case 1: # Add user.
                    user_manager.create_user()
                case 2: # Load user. TO-DO
                    pass 
                case 3: # List users. TO-DO
                    pass
                case 4: # Quit.
                    terminal.clear_console()
                    print("Exiting...")
                    exit()
        except Exception as error:
            print(error)