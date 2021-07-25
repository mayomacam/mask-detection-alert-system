import os
import smtplib
#instead of providing email adress and password in python program
#We are passing these credential using sytem environment variables for security purpose

EMAIL_ADDRESS = os.environ.get('testingfacemasksys@gmail.com') 
#it will get value of system environment variables named "EMAIL_USER"
EMAIL_PASSWORD = os.environ.get('@testtesttest4269#')
#it will get value of system environment variables named "EMAIL_PASS" saved in local system


#Using context manager we will make sure that our connection is closed automatically
#Email is submitted by a mail client (mail user agent, MUA) to a mail server (mail submission agent, MSA) using SMTP on TCP port 587
#SMTP servers commonly use the Transmission Control Protocol on port number 25 (for plaintext) and 587 (for encrypted communications).
# 'smtp.gmail.com for google mail service and we can use our localhost to send test email.
with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
    #ehlo() method identifies ourself with the mail server that we are using
    smtp.ehlo()
    #Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted.
    # You should then call ehlo() again
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #Header of mail
    subject = "Face Mask Voilation"
    #body of mail
    body = "One Visitor voilated Face Mask Policy. He is not wearing the mask"
    #to construct the plaintext email we will add subject as header and then after couple of blank line
    #we will input body of email and we are using fstring for this
    msg = f' Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS,msg)
#in order to send the email through python using gmail account we have to do some setting in our gmail account
#We have to turn on less secure app access and have to remove two factor authentication in gmail account
#We are using a demo gmail id to send the message.
