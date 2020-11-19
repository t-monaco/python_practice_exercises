import re

phone_regex = re.compile(r'(\d{3})\-(\d{3}\-\d{4})')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
mo = phone_regex.search(message)
area_code, phone_number = mo.groups()
print(area_code, phone_number)
