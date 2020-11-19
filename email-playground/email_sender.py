import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./index.html').read_text())
email = EmailMessage()
email['from'] = 'TechHUB'
email['to'] = 'monacotomas99@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

# email.set_content(html.substitute(name='Tomas'), 'html')
email.set_content(html.substitute({'name': 'Tomas'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('techhub.arg@gmail.com', 'tech19HUB')
    smtp.send_message(email)

print('Done!')

# ! *********************************************************************
# ! *********************************************************************
# ! ** MAKE AN "ENV" IN ORDER TO READ VARIABLES SUCH AS usr & password **
# ! *********************************************************************
# ! *********************************************************************
