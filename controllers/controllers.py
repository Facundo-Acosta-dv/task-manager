# controllers.py
import uuid, time, json
from utils import debug_log 

class Controller:

    # Returns time as a string.
    def get_time(self):
        return time.strftime("%X")

    # Returns date as a string.
    def get_date(self):
        return time.strftime("%d/%m/%y")

    # Generates a UUID.
    def generate_id(self):
        new_id = str(uuid.uuid4())
        debug_log(f"new id: {new_id}")
        return new_id

    # Checks if the input is an integer.
    def validate_integer(self, prompt_text='No prompt text has been given (validate_integer): ', value_error_text="", clear_on_fail=False, header_text=""):
        from views.terminal import Terminal

        terminal = Terminal()
        
        while True:
            try:
                if header_text: print(header_text) # Prints header text
                user_input = int(input(prompt_text))
                return user_input
            except ValueError:
                if clear_on_fail:
                    terminal.clear_console()
                if value_error_text:
                    print(str(value_error_text))

    # Validates integer based on range given.
    def int_in_range(self, min, max, prompt_text=f"int_in_range({min}~{max}):", out_of_range_text="", value_error_text="", clear_on_fail=False, header_text=""):
        from views.terminal import Terminal
        terminal = Terminal()

        while True:
            user_input = self.validate_integer(prompt_text, value_error_text, clear_on_fail, header_text)

            if user_input >= min and user_input <= max:
                return user_input
            else:
                if clear_on_fail:
                    terminal.clear_console() # Clears console if arg clear_on_fail is enabled. 
                if out_of_range_text:
                    print(str(out_of_range_text))

    # Asks a yes or no question
    def yes_or_no(self, prompt_text='No prompt text has been provided! (Yes or No): ', error_text='No error text has been provided (Yes or No): '):
        while True:
            user_input = str(input(str(prompt_text)))
            if user_input.strip().lower() in ['yes', 'y']:
                return True
            elif user_input.strip().lower() in ['no', 'n']:
                return False
            else:
                print(str(error_text))
    
    # Checks if any character is a string based on an input.
    def validate_string(self, prompt_text='No prompt has been text provided! ', error_text='No error text has been provided! '):
        while True:
            user_input = str(input(prompt_text))
            if any(char.isdigit() for char in user_input):
                print(str(error_text))
            else:
                return user_input
            
    # Creates a .json file in the current directory.
    def create_json(self, filename, content=""):
        if filename.endswith(".json"): # Checks if "filename" ends with ".json" and removes it from the string.
            filename = filename.replace(".json", "")
        try: # Makes a file with the filename given as a .json.
            with open(str(f"{filename}.json"), "w") as file:
                json.dump(content, file, indent= 4)
                debug_log(f".json file created: {filename}.json with the content {content} and indent= 4.")
                return content
        except Exception as error: # Raises an exception if something goes wrong making the file.
            print(f"Error: an error has ocurred: {error}")

    # Gives the menu options and returns a number based on input.
    def menu_options(self, min, max, prompt_text="prompt_text_input_val", out_of_range_text="out of range", value_error_text="please, enter a valid number"):
        from views.view import View
        view = View()
        header = view.main_menu_header()
        return self.int_in_range(min, max, prompt_text, out_of_range_text, value_error_text, True, header)

        
        
                    
            
            