# utils.py (common utilities module)

# Enables debug if Global DEBUG = True.
def debug_log(debug_message, capitalize=True):
    import config
    if capitalize and isinstance(debug_message, str):
        debug_message = debug_message.capitalize()
    if config.DEBUG:
        print(f'[DEBUG] {debug_message} [DEBUG]')
    