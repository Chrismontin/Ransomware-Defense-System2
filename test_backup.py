from modules.backup_manager import backup_files

success, message = backup_files()

print(success)
print(message)