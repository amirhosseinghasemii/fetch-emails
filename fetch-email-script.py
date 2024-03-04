import email
import imaplib

# main script
user = 'backupreport11@gmail.com'
password = 'jcbw bmmg zcio fldx'
host = 'imap.gmail.com'

# Connect securely with SSL
imap = imaplib.IMAP4_SSL(host)

# Login to remote server
imap.login(user, password)
imap.select('Inbox')
status, data = imap.search(None, 'unseen')

mail_ids = []
for block in data:
    mail_ids += block.split()

# fetch and import emails in a loop
for i in mail_ids:
    status, forCheck = imap.fetch(i, '(RFC822)')
    for response_part in forCheck:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_subject = message['subject']
            if message.is_multipart():
                mail_content = ''

                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()
            print(mail_content)