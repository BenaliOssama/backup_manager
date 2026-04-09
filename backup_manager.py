import os
from datetime import datetime


SCHEDULE_FILE = "backup_schedules.txt"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "backup_manager.log")
BACKUP_DIR = "backups"
PID_FILE = "backup_service.pid"


# ---------------- Logging ---------------- #
def log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")


# ---------------- Schedule Utils ---------------- #
def validate_schedule(schedule):
    try:
        path, time_str, name = schedule.split(";")
        datetime.strptime(time_str, "%H:%M")
        return path and name
    except:
        return False
