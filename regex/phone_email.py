#! Python 3
# * Find phone numbers and email address on the clipboard

import pyperclip
import re

text = str(pyperclip.paste())

regex_phone = re.compile(r'''(
    \(?(\d{,3})\)?      # area code
    [- |\s |\.]?        # first separator
    (\d{3})             # first 3 numbers
    [- |\s |\.]?        # second separator
    (\d{4})             # last 4 numbers
    )''', re.VERBOSE)

regex_email = re.compile(r'''(
    ([\w\d\._\-+%]+)    # username
    @                   # @ symbol
    ([\w\d\.\-]+)       # domain name
    (\.[\w]{2,4})       # dot something
    )''', re.VERBOSE)


matches = []

for groups in regex_phone.findall(text):
    phone_num = '-'.join([groups[1], groups[2], groups[3]]) # * format phone number
    matches.append(phone_num)

for groups in regex_email.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy to clipboard:')
    print('\n'.join(matches))
else:
    print('No email addresses or phone numbers found.')
