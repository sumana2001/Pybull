# Use terminal to run this script else getpass may not work & throw an error
# To use gmail account to send bulk emails, enable access for less secure apps for that account

import smtplib
import ssl
import csv
import getpass
import time
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 

def sendMail():
    port = 465 #port for gmail
    senderEmailID = input("Email ID: ")
    password = getpass.getpass("Password: ") # to securely accept user password
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(senderEmailID, password)
        print("Login Successful")
        time.sleep(2)
        subject = input("Enter subject: ")
        path = input("Enter path to csv file: ")
        with open(path) as file:
            reader = csv.reader(file)
            next(reader)  # to skip header row
            for name, email in reader:
                msg = MIMEMultipart()
                msg['From'] = senderEmailID
                msg['To'] = email
                msg['Subject'] = subject
                body = "Hi {name}! Welcome to Python!" 
                msg.attach(MIMEText(body.format(name = name), 'plain'))
                text = msg.as_string()
                server.sendmail(senderEmailID, email, text)
                print(f'Sent to {name} ({email})')

if __name__=='__main__':
    sendMail()
