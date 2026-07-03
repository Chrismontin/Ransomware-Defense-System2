import time

from config.settings import THRESHOLD
from config.settings import TIME_WINDOW

# Stores timestamps of recent events
event_history = []


def analyze_event():
    """
    Checks whether the number of events within
    the configured time window exceeds the threshold.
    """

    current_time = time.time()

    event_history.append(current_time)

    # Remove old events
    event_history[:] = [
        t for t in event_history
        if current_time - t <= TIME_WINDOW
    ]

    if len(event_history) >= THRESHOLD:
        return True, len(event_history)

    return False, len(event_history)