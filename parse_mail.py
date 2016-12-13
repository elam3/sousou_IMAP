# -*- coding: utf-8 -*-
from __future__ import print_function
import sys , imaplib , getpass , email , datetime
from os import environ
from dotenv import load_dotenv
email_default_encoding = 'ISO-2022-JP'

# Load .env credentials
load_dotenv('.env')
EMAIL_ADDRESS = environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = environ.get('EMAIL_PASSWORD')
EMAIL_LABEL = environ.get('EMAIL_LABEL')

# Need to enable "less secure apps" on gmail for login success
gmail = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    print("Logging in...", end="")
    res, data = gmail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    print(res, "\t", data[0]) # Login Successful
except:
    print("Failed to login.")
    sys.exit(1)

print("Selecting label...", end="")
res, data = gmail.select(EMAIL_LABEL) # Choose a gmail label
if res == "OK":
    print(res, "\t", data[0])
else:
    print("Error selecting label \"", EMAIL_LABEL, "\"")
    sys.exit(1)

mailbox = []

#process_mailbox(gmail)
res, data = gmail.search(None, "ALL")
if res != "OK":
    print("No messages found.")
    gmail.close()
    gmail.logout()
    sys.exit(1)

for itr in data[0].split():
    mailbox.append( gmail.fetch(itr, "(RFC822)") )
#end for

res, data = gmail.close()
print(res,"\t", data)
res, data = gmail.logout()
print(res,"\t", data)

for res, mail in mailbox:
    raw_email = mail[0][1]
    msg = email.message_from_string(raw_email)
    body = raw_email

    # TODO : get rid of the dos newline chars \r\n
    # Getting error about dos2unix cannot run on binary file
    '''
    #msg = email.message_from_string(raw_email.decode('utf-8'))
    msg_encoding = 'ISO-2022-JP'
    #msg = email.message_from_string(raw_email.decode(msg_encoding))
    body = msg.get_payload()
    body = raw_email if len(body)==0 else body
    '''

    # File Naming Format -- shipmentYYYYMMDD.html
    date_tuple = email.utils.parsedate_tz(msg['Date'])
    YYYY = str(date_tuple[0])
    MM = str(date_tuple[1])
    MM = MM if len(MM)==2 else "0"+MM
    DD = str(date_tuple[2])
    DD = DD if len(DD)==2 else "0"+DD
    filename = 'docs/shipment'+YYYY+MM+DD+'.html'

    with open(filename, 'wb') as f_out:
        f_out.write(body)
#end for


