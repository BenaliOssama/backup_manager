# Clean slate
rm -rf logs backups backup_schedules.txt

# Create a test folder to back up
mkdir testing
touch testing/file1 testing/file2 testing/file3

# Add a schedule for the CURRENT minute (check your clock first)
python3 ./backup_manager.py create "testing;15:17;backup_test"

# List schedules
python3 ./backup_manager.py list

# Start the service
python3 ./backup_manager.py start

# Wait a moment, then check backups
python3 ./backup_manager.py backups

# Check the logs
cat logs/backup_manager.log
cat logs/backup_service.log

# Stop the service
python3 ./backup_manager.py stop
