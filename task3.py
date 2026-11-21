import re

PHONE_RE = re.compile(r"^\+7-\d{3}-\d{3}-\d{2}-\d{2}$")
DATE_RE = re.compile(r"^(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$")

def check(pattern, value):
    return bool(pattern.match(value))

print(check(PHONE_RE, "+7-900-111-22-33"))
print(check(PHONE_RE, "8-900-111-22-33"))
print(check(DATE_RE, "31.12.2025"))
print(check(DATE_RE, "32.12.2025"))