from datetime import datetime


def current_timestamp():
    """
    Returns the current date and time
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")