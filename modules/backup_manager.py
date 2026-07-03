import os
import shutil

from config.settings import WATCH_FOLDER
from config.settings import BACKUP_FOLDER


def backup_files():
    """
    Creates or updates a backup of the monitored files.
    """

    try:

        if not os.path.exists(WATCH_FOLDER):
            return False, "Watch folder does not exist."

        os.makedirs(BACKUP_FOLDER, exist_ok=True)

        shutil.copytree(
            WATCH_FOLDER,
            BACKUP_FOLDER,
            dirs_exist_ok=True
        )

        return True, "Backup completed successfully."

    except Exception as e:
        return False, str(e)