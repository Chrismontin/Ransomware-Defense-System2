from modules.logger import initialize_logs
from modules.logger import write_event
from modules.logger import write_alert

initialize_logs()

write_event("Logger Test Successful")

write_alert("Alert Test Successful")

print("Logger working correctly.")