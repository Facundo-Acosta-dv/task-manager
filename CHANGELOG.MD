# Changelog

## 2024-09-17

- Added function `create_json`.
- Refactored the functions `load_users`, `create_user` and `add_user`
- User now records the time and date of creation.
- Improved error handling.
- Added `README.MD`.

## 2024-09-19
### Added 
- Added functions `main_menu`, `validate_int_range`, `menu_input` and `main_menu_header` in order to implement a menu system.
- Introduced `utils.py` to resolve potential circular imports.
  
### Changed
- Renamed class `TaskView` to `View` for simplicity.
- Function `debug_log()` is now a part of `utils.py`.
- Function `clear_console()` is now disabled by default and can be re-enabled in the configuration file of the project.
- Added `.gitignore` file.
- Removed cache files.
