# Fetch Mail
This python script was an intro to IMAP for me. The goal was to fetch mail from my google account and write out to physical files for parsing later.

## Development Environment
Python 2.7.12
click==6.6
python-dotenv==0.6.1

### .env sample
```bash
EMAIL_ADDRESS=''
EMAIL_PASSWORD=''
EMAIL_LABEL=''
```

> Note: Don't forget to rename sample and `chmod 600 .env`

> Potential Issue: I had to delete the quotes marks on the right hand side because `EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")` included the single-quotes inside the string


## Resources
* http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
* https://gist.github.com/robulouski/7441883
* http://qiita.com/stkdev/items/a44976fb81ae90a66381
