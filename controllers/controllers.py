# controllers.py
import config, uuid, time, json

class Controller:
    
    # Initializes the constructor
    def __init__(self) -> None:
        pass
    
    # Enables debug if Global DEBUG = True
    def debug_log(self, debug_message, capitalize=True):
        if capitalize and isinstance(debug_message, str):
            debug_message = debug_message.capitalize()
        if config.DEBUG:
            print(f'[DEBUG] {debug_message} [DEBUG]')
    
    # TO-DO func to return time
    def get_time(self):
        return time.strftime("%X")

    def get_date(self):
        return time.strftime("%d/%m/%y")

    # Generates a new ID number
    def generate_id(self):
        new_id = str(uuid.uuid4())
        self.debug_log(f"new id: {new_id}")
        return new_id

    # Checks if the input is an integer
    def validate_integer(self, prompt_text='No prompt text has been given (validate_integer): ', error_text='No error text has been provided! (validate_integer): '):
        while True:
            try:
                user_input = int(input(prompt_text))
                return user_input
            except ValueError:
                print(str(error_text))
        
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
    
    # Checks if any character is a string based on an input
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
                self.debug_log(f".json file created: {filename}.json with the content {content} and indent= 4.")
                return content
        except Exception as error: # Raises an exception if something goes wrong making the file.
            print(f"Error: an error has ocurred: {error}")
            
            