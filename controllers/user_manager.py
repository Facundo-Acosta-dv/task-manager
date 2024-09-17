# person_manager.py
from models.user import User
from controllers.controllers import Controller
import os, json

controller = Controller()

class UserManager:

    # Initializes constructor.
    def __init__(self):
        pass

    # TO-DO FACTORIZE ALL INSIDE THIS FUNCTION TO METHODS - Loads "users.json" file.
    def load_users(self):
        # TO-DO ASKS IF THE USER WANTS TO CREATE "users.json" IF IT DOESN'T EXIST - Creates "users.json" if it doesn't exists and returns an empty list.
        if not os.path.exists("users.json"):
            with open("users.json", "w") as file:
                json.dump([], file, indent=4)
                controller.debug_log("creating 'users.json")
                return []
        else: # Loads "users.json" file and returns it.
            with open("users.json", "r") as file:
                content = file.read().strip()
                if content:
                    users_file = json.loads(content)
                    return users_file
                else:
                    controller.debug_log("'users.json' is empty or contains only whitespaces, returning [].")
                    return []

    # Checks if an user exists based on ID given.  
    def user_exists(self, user_id):
        users = self.load_users()
        return any(user.get("id") == str(user_id) for user in users)
            
    # Saves "users.json" file.
    def save_users(self, users):
        controller.debug_log(users)
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
            controller.debug_log("users overwritten")
        
    # Adds a user to the list.
    def add_user(self, new_user):
        controller.debug_log("Start of function add_user... ")
        users_file = self.load_users()
        controller.debug_log(f"users_file --> {users_file}")
        controller.debug_log(f"new_user--> {new_user.__dict__}")
        users_file.append(new_user.__dict__)
        self.save_users(users_file)
         
    # Saves user data to JSON file.
    def save_user(self, user):
        user_data = {
            'username': user.username,
            'id': user.user_id,
            'age': user.age,
            'tasks': user.tasks,
        }
        filename = f'user_{user.user_id}_data.json'
        controller.debug_log(f"user data:\n{user_data}")
        with open(filename, 'w') as file:
            json.dump(user_data, file, indent=4)
            controller.debug_log("user saved successfully")
    
    # Loads an user from "users.json".
    def load_user(cls, user_id):
        users = cls.load_users()
        for _, user in enumerate(users): # Iterates users.json in search of an user with the ID provided.
            if user.get("id") == str(user_id):
                controller.debug_log(user)
                controller.debug_log(f"user {user.get('username')} found with id {user_id}")
                controller.debug_log(f"returning user...")
                return user # Returns user dict and the index in "users.json" file.
        print("User not found! ")
    
    # Creates an user based on username and age inputs | TO-DO --> Validate that the username doesn't already exists.
    def create_user(self):
        username = str(input('Enter your username: ')).strip()
        age = controller.validate_integer("Enter your age: ", "Please, enter a valid age! ")
        id = controller.generate_id()
        new_user = User(username, age, id)
        self.add_user(new_user)
        print(f'User "{username}" has been created successfully! ')



        