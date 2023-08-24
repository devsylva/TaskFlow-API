import os
import subprocess
import datetime
import boto3

# Django project settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskflow.settings")

# Directory to store backup files locally
backup_dir = "C:\Users\USER\Desktop\PROJECTS\TaskFlow-API\backups\backup.json"

# Amazon S3 configuration
s3_bucket_name = "your-s3-bucket-name"
s3_folder = "task_backups/"

# Run Django's dumpdata command
backup_file_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_backup.json"
backup_file_path = os.path.join(backup_dir, backup_file_name)
subprocess.run(["python", "manage.py", "dumpdata", "task_app", "--output", backup_file_path])

# Upload backup to S3
s3_client = boto3.client("s3")
s3_key = os.path.join(s3_folder, backup_file_name)
s3_client.upload_file(backup_file_path, s3_bucket_name, s3_key)

# Clean up local backup file
os.remove(backup_file_path)

print("Backup completed and uploaded to S3:", s3_key)
