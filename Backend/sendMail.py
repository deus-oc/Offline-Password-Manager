from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

# to be hardcoded
from dotenv import load_dotenv

load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
PASSWORD = os.getenv('PASSWORD')


class SendMail():

    def __init__(self):
        self.sender = EMAIL_ADDRESS
        self.senderPassword = PASSWORD
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.sender, self.senderPassword)

    # Order of parameters matter
    def send(self, reciever, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = reciever
        msg['subject'] = subject
        Message = message
        msg.attach(MIMEText(Message, 'plain'))
        text = msg.as_string()
        self.server.sendmail(self.sender, reciever, text)
        return
