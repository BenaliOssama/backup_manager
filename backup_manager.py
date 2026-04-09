import sys
import os
from datetime import datetime

LOG_FILE = "./logs/backup_manager.log"

def log(message):
    os.makedirs("./logs", exist_ok=True)
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    entry = f"{timestamp} {message}\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def cmd_create(schedule):
    pass

def cmd_list():
    pass

def cmd_delete(index):
    pass

def cmd_start():
    pass

def cmd_stop():
    pass

def cmd_backups():
    pass

def main():
    if len(sys.argv) < 2:
        log("Error: no command provided")
        return

    command = sys.argv[1]

    if command == "create":
        cmd_create(sys.argv[2])
    elif command == "list":
        cmd_list()
    elif command == "delete":
        cmd_delete(sys.argv[2])
    elif command == "start":
        cmd_start()
    elif command == "stop":
        cmd_stop()
    elif command == "backups":
        cmd_backups()
    else:
        log(f"Error: unknown instruction")

main()
