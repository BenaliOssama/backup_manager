import sys
import os
import subprocess
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


# ---------------- Commands ---------------- #
def create(schedule):
    try:
        if not validate_schedule(schedule):
            raise ValueError

        with open(SCHEDULE_FILE, "a") as f:
            f.write(schedule + "\n")

        log(f"New schedule added: {schedule}")

    except:
        log(f"Error: malformed schedule: {schedule}")


def list_schedules():
    try:
        with open(SCHEDULE_FILE) as f:
            lines = f.readlines()

        log("Show schedules list")

        for i, line in enumerate(lines):
            print(f"{i}: {line.strip()}")

    except:
        log("Error: can't find backup_schedules.txt")


def delete(index):
    try:
        with open(SCHEDULE_FILE) as f:
            lines = f.readlines()

        index = int(index)

        if index < 0 or index >= len(lines):
            raise IndexError

        removed = lines.pop(index)

        with open(SCHEDULE_FILE, "w") as f:
            f.writelines(lines)

        log(f"Schedule at index {index} deleted")

    except FileNotFoundError:
        log("Error: can't find backup_schedules.txt")
    except:
        log(f"Error: can't find schedule at index {index}")


def start():
    try:
        if os.path.exists(PID_FILE):
            log("Error: backup_service already running")
            return

        process = subprocess.Popen(
            ["python3", "backup_service.py"],
            start_new_session=True
        )

        with open(PID_FILE, "w") as f:
            f.write(str(process.pid))

        log("backup_service started")

    except:
        log("Error: can't start backup_service")


def stop():
    try:
        if not os.path.exists(PID_FILE):
            raise Exception

        with open(PID_FILE) as f:
            pid = int(f.read())

        os.kill(pid, 9)
        os.remove(PID_FILE)

        log("backup_service stopped")

    except:
        log("Error: can't stop backup_service")


def backups():
    try:
        files = os.listdir(BACKUP_DIR)
        log("Show backups list")

        for f in files:
            print(f)

    except:
        log("Error: can't find backups directory")


# ---------------- Main ---------------- #
def main():
    if len(sys.argv) < 2:
        log("Error: invalid command")
        return

    command = sys.argv[1]

    if command == "create" and len(sys.argv) == 3:
        create(sys.argv[2])
    elif command == "list":
        list_schedules()
    elif command == "delete" and len(sys.argv) == 3:
        delete(sys.argv[2])
    elif command == "start":
        start()
    elif command == "stop":
        stop()
    elif command == "backups":
        backups()
    else:
        log("Error: invalid command")


if __name__ == "__main__":
    main()