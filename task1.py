import re

text = "Contact: ivan@example.com, anna@test.ru"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
print(emails)