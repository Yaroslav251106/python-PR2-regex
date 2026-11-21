import re

log = """\
2025-11-12 10:15:00 INFO  user 'ivan' logged in from 192.168.10.5
2025-11-12 10:17:22 ERROR user 'anna' failed login from 10.0.0.77
2025-11-12 10:20:11 INFO  user 'oleg' logged in from 192.168.10.9
2025-11-12 10:22:45 ERROR user 'guest' blocked from 172.16.1.4
"""

pattern = re.compile(r"^(\S+ \S+) ERROR .* from (\d+\.\d+\.\d+\.\d+)$", re.MULTILINE)
for dt, ip in pattern.findall(log):
    print(f"{dt} -> {ip}")