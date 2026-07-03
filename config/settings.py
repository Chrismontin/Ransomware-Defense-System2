"""
Global configuration settings for the Ransomware Defense System
"""

# ==========================
# Server Configuration
# ==========================
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}/event"

# ==========================
# Folder Paths
# ==========================
WATCH_FOLDER = "test_files"

BACKUP_FOLDER = "backup"

RECOVERY_FOLDER = "recovery"

LOG_FOLDER = "logs"

# ==========================
# Log Files
# ==========================
EVENT_LOG = "logs/file_events.log"

ALERT_LOG = "logs/alerts.log"

# ==========================
# Detection Parameters
# ==========================
THRESHOLD = 10

TIME_WINDOW = 10

# ==========================
# Dashboard
# ==========================
AUTO_REFRESH = 2000