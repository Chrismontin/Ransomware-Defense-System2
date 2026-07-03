import time
import requests

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config.settings import WATCH_FOLDER
from config.settings import SERVER_URL

from modules.utils import current_timestamp


class FileMonitor(FileSystemEventHandler):

    def send_event(self, event_type, file_path):

        payload = {
            "timestamp": current_timestamp(),
            "event_type": event_type,
            "file_path": file_path
        }

        try:
            response = requests.post(
                SERVER_URL,
                json=payload,
                timeout=3
            )

            print(
                f"[{response.status_code}] "
                f"{event_type.upper()} -> {file_path}"
            )

        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to the Flask server.")

        except Exception as e:
            print(f"Error: {e}")

    def on_created(self, event):

        if not event.is_directory:
            self.send_event("created", event.src_path)

    def on_modified(self, event):

        if not event.is_directory:
            self.send_event("modified", event.src_path)

    def on_deleted(self, event):

        if not event.is_directory:
            self.send_event("deleted", event.src_path)

    def on_moved(self, event):

        if not event.is_directory:
            self.send_event("moved", event.dest_path)


if __name__ == "__main__":

    observer = Observer()

    handler = FileMonitor()

    observer.schedule(
        handler,
        WATCH_FOLDER,
        recursive=True
    )

    observer.start()

    print("=" * 50)
    print("Ransomware Monitoring Agent Started")
    print("=" * 50)
    print(f"Watching folder: {WATCH_FOLDER}")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()