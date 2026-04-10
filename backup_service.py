import os
import time
import tarfile
from datetime import datetime

LOG_FILE = "./logs/backup_service.log"
SCHEDULES_FILE = "./backup_schedules.txt"
BACKUPS_DIR = "./backups"

def log(message):
    os.makedirs("./logs", exist_ok=True)
    timestamp = datetime.now().strftime("[%d/%m/%Y %H:%M]")
    entry = f"{timestamp} {message}\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def do_backup(path, name):
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    tar_path = f"{BACKUPS_DIR}/{name}.tar"
    with tarfile.open(tar_path, "w") as tar:
        tar.add(path)
    log(f"Backup done for {path} in {tar_path}")

def run():
    while True:
        try:
            with open(SCHEDULES_FILE, "r") as f:
                lines = f.readlines()

            now = datetime.now().strftime("%H:%M")
            remaining = []

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                if len(parts) != 3:
                    continue
                path, scheduled_time, name = parts
                if scheduled_time == now:
                    try:
                        do_backup(path, name)
                    except Exception as e:
                        log(f"Error: backup failed for {path}: {e}")
                else:
                    remaining.append(line + "\n")

            with open(SCHEDULES_FILE, "w") as f:
                f.writelines(remaining)

        except FileNotFoundError:
            log("Error: cannot open backup_schedules")

        time.sleep(45)

run()
