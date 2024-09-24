# pip install psutil before running the code

import psutil
import logging
import time

# Set thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 300  # number of processes

# Setup logging to a file
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_alert(message):
    """ Log alerts to both the console and a file """
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"ALERT: High Memory usage detected: {memory_usage}%")

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"ALERT: Low Disk space detected: {disk_usage}% used")

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_alert(f"ALERT: High number of running processes: {process_count}")

def monitor_system_health():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_space()
        check_running_processes()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    log_alert("Starting System Health Monitoring")
    monitor_system_health()
