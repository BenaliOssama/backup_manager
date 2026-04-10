# Clean slate first
rm -rf logs backups backup_schedules.txt

# 1. Try to stop a service that isn't running
python3 ./backup_manager.py stop

# 2. Try a malformed schedule
python3 ./backup_manager.py create "wrong_format"

# 3. Try to list backups when backups/ doesn't exist
python3 ./backup_manager.py backups

# 4. Start the service
python3 ./backup_manager.py start

# 5. Try to start it again while it's already running
python3 ./backup_manager.py start

# 6. Try an unknown command
python3 ./backup_manager.py invalid_command

# Check both logs
cat logs/backup_manager.log
cat logs/backup_service.log
