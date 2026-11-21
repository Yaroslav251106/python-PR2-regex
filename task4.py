import re

log = "2025-11-12 14:30:05 ERROR User 'ivan' failed login from 192.168.10.5"

pattern = re.compile(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) .* from (\d+\.\d+\.\d+\.\d+)")
m = pattern.search(log)
if m:
    date, time, level, ip = m.groups()
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Level: {level}")
    print(f"IP: {ip}")