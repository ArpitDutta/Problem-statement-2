# Assuming the log file follows a common Apache or Nginx format
# 127.0.0.1 - - [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1024
# 127.0.0.1 - - [10/Oct/2024:13:56:01 +0000] "GET /about.html HTTP/1.1" 404 512

import re
from collections import Counter

# Path to the log file (change this to your log file path)
log_file_path = 'webserver.log'

# Regular expression to parse the log entries
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>\S+) HTTP/\d+\.\d+" (?P<status>\d+) (?P<size>\d+)'
)

# Counters to track data
status_counter = Counter()
page_counter = Counter()
ip_counter = Counter()

# Function to parse and analyze the log file
def analyze_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                
                # Track status codes (e.g., count 404 errors)
                status_counter[data['status']] += 1
                
                # Track requested pages (URLs)
                page_counter[data['url']] += 1
                
                # Track IP addresses
                ip_counter[data['ip']] += 1

# Function to generate a summary report
def generate_report():
    print("----- Web Server Log Report -----")
    
    # 1. Number of 404 errors
    print(f"\nTotal 404 Errors: {status_counter.get('404', 0)}")
    
    # 2. Most requested pages
    most_requested_pages = page_counter.most_common(5)
    print("\nTop 5 Most Requested Pages:")
    for page, count in most_requested_pages:
        print(f"{page}: {count} requests")
    
    # 3. IP addresses with the most requests
    top_ips = ip_counter.most_common(5)
    print("\nTop 5 IP Addresses with Most Requests:")
    for ip, count in top_ips:
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    analyze_log_file(log_file_path)
    generate_report()
