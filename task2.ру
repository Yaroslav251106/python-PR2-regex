import re

EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]{2,}$")

def is_valid_email(s: str) -> bool:
    return bool(EMAIL_RE.match(s))

tests = [
    "ivan@example.com",
    "anna@test.ru",
    "bad@",
    "@missing.com",
    "ok.name+tag@mail.co"
]
for t in tests:
    print(f"{t:35} -> {is_valid_email(t)}")