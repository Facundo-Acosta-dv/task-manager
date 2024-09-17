# terminal.py
import os, platform

class Terminal:
    
    # Initializes constructor
    def __init__(self):
        pass

    # Clears console based on Operating System
    def clear_console(self):
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
    
    # i dont know what the fuck is this shit
    def system_info(self):
        print(platform.system())