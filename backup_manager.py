import os

SCHEDULE_FILE = "backup_schedules.txt"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "backup_manager.log")
BACKUP_DIR = "backups"
PID_FILE = "backup_service.pid"
