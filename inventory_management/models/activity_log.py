
import datetime

def log_activity(activity):
    with open("activity_log.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {activity}\n")

def view_logs():
    try:
        with open("activity_log.txt", "r") as file:
            logs = file.readlines()
            for log in logs:
                print(log.strip())
    except FileNotFoundError:
        print("No activity logs found.")
