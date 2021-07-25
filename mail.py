#from email.message import EmailMessage
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from tkinter import * 
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import base64, mimetypes
import random, string

#scopes or given permission access links
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


class Emailalert():
    def __init__(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret_63063835404-8kv353utgq13uvfv1vea71vsdhhd8r64.apps.googleusercontent.com.json', SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

        self.service = build('gmail', 'v1', credentials=creds)
    

        """# create mail data
        to = 'amanrkt231217@gmail.com'
        message_text = '''Hey there!
            I'm testing my first gmail api message'''
        message = create_message(to, message_text)
        print(message)"""

    def send_message(self, message):
        # Call the Gmail API
        try:
            message_send = (self.service.users().messages().send(userId='me', body=message).execute())
            print('Message Id: %s' % message_send['id'])
        except errors.HttpError:
            print('An error occurred: %s' % error)
        with open('mesg.txt', 'w') as mesg:
            mesg.write(str(message_send))
    
        # show a message about mail sent
        root = Tk()
        root.geometry("300x200")
        messagebox.showinfo("showinfo", "Alert send!")

        #def create_message(sender, to, subject, message_text):
    def create_message(self, to, message_text, seed_num, file):
        """Create a message for an email.
        Returns:
        An object containing a base64url encoded email object.
        """

        """message = MIMEText(message_text)
        message['to'] = to
        message['from'] = 'amanrkt231217@gmail.com'
        message['subject'] = '#{} Test message from {} to {}!'.format(seed_num, message['from'], message['to'])
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}"""

        """above line use when only send text
           use below when sending a attachment"""
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = 'amanrkt231217@gmail.com'
        message['subject'] = '#{} alert message from {} to {}!'.format(seed_num, message['from'], message['to'])

        msg = MIMEText(message_text)
        message.attach(msg)

        content_type, encoding = mimetypes.guess_type(file)

        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

"""if __name__ == '__main__':
    main()"""

a = Emailalert()
#adding a verify number from my side to keep check the data
seed_num = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print('seed number is: '+seed_num)
# create mail data
to = 'testingfacemasksys@gmail.com'
file = '2.jpg'
message_text = """Hey there!
    System alert no mask #""" + seed_num
message = a.create_message(to, message_text, seed_num, file)
#print(message)
print('seed number is: '+seed_num)
a.send_message(message)
