# Backup Manager

A Python-based automated backup system that schedules and performs compressed directory backups from the command line.

## How It Works

Two scripts work together:

- `backup_manager.py` — the CLI control panel. You interact with this directly to manage schedules and control the service.
- `backup_service.py` — the background worker. Once started, it runs silently, checks the schedule every 45 seconds, and performs backups when the time matches.

Schedules are stored in `backup_schedules.txt` — the shared file both scripts read and write. All actions are logged to the `logs/` directory.

## Project Structure

```
backup-manager/
├── backup_manager.py        # CLI script for managing schedules and service
├── backup_service.py        # Background service that performs scheduled backups
├── logs/                    # Created at runtime
│   ├── backup_manager.log
│   └── backup_service.log
├── backups/                 # Created at runtime
├── backup_schedules.txt     # Created at runtime
└── README.md
```

## Usage

### Add a backup schedule

```bash
python3 backup_manager.py create "path_to_folder;HH:MM;backup_name"
```

Example:
```bash
python3 backup_manager.py create "project;18:30;project_backup"
```

The schedule format is `path;HH:MM;backup_name`. All three fields are required.

### List all schedules

```bash
python3 backup_manager.py list
```

Output example:
```
0: project;18:30;project_backup
1: docs;19:00;docs_backup
```

### Delete a schedule by index

```bash
python3 backup_manager.py delete 1
```

### Start the background service

```bash
python3 backup_manager.py start
```

The service runs in the background and checks schedules every 45 seconds.

### Stop the background service

```bash
python3 backup_manager.py stop
```

### List completed backups

```bash
python3 backup_manager.py backups
```

## Schedule Behavior

- Backups are **one-shot** — once a scheduled backup runs, the schedule is removed.
- If the service is not running when a scheduled time passes, that backup will not run.
- Schedules with a past time are kept in the file but never triggered.
- Backups are saved as `.tar` files in the `./backups/` directory.

## Logging

All actions and errors are logged with timestamps in the format `[dd/mm/yyyy hh:mm]`.

- `logs/backup_manager.log` — logs every command run through the manager
- `logs/backup_service.log` — logs every backup performed or failed

## Example Session

```bash
# Create schedules
python3 backup_manager.py create "project;18:30;project_backup"
python3 backup_manager.py create "docs;18:30;docs_backup"

# Verify
python3 backup_manager.py list

# Start the service
python3 backup_manager.py start

# After scheduled time passes, check results
python3 backup_manager.py backups

# Stop the service
python3 backup_manager.py stop
```

## Requirements

- Python 3
- Linux/Unix environment
