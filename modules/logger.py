import os

from config.settings import EVENT_LOG
from config.settings import ALERT_LOG


def initialize_logs():
    """
    Creates log files if they don't exist.
    """

    os.makedirs("logs", exist_ok=True)

    for logfile in [EVENT_LOG, ALERT_LOG]:
        if not os.path.exists(logfile):
            with open(logfile, "w", encoding="utf-8"):
                pass


def write_event(message):
    with open(EVENT_LOG, "a", encoding="utf-8") as log:
        log.write(message + "\n")


def write_alert(message):
    with open(ALERT_LOG, "a", encoding="utf-8") as log:
        log.write(message + "\n")