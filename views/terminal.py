# terminal.py
import os

class Terminal:
    
    # Initializes constructor
    def __init__(self):
        pass

    # Clears console based on Operating System
    def clear_console(self):
        from utils import debug_log
        import config
        if config.ENABLE_CLEAR:
            if self.system_info() == 'Windows':
                debug_log(self)
                clear = str('cls')
            else:
                clear = str('clear')
            os.system(clear)
            debug_log(f"Detected {self.system_info()} system, cleared terminal with '{clear}'")
    
    # Returns system info.
    def system_info(self):
        import platform; return platform.system()