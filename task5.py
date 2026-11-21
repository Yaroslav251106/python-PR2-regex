import re

raw = "Call +7-900-111-22-33 or +7-900-444-55-66 tomorrow."
masked = re.sub(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", "[PHONE]", raw)
print(masked)

text = "line1   with   spaces\nline2\twith\ttabs"
clean = re.sub(r"\s+", " ", text)
print(clean)

parts = re.split(r"\s*,\s*", "one, two ,three , four")
print(parts)