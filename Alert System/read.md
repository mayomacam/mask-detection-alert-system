# EMAIL ALERT
* The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP
* class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)
An SMTP instance encapsulates an SMTP connection. It has methods that support a full repertoire of SMTP and ESMTP operations. If the optional host and port parameters are given, the SMTP connect() method is called with those parameters during initialization.
* <u>Context Manager in connecting to Email Server:-</u>
The SMTP class supports the with statement. When used like this, the SMTP QUIT command is issued automatically when the with statement exits

* SMTP.ehlo(name='')
Identify yourself to an ESMTP server using EHLO. The hostname argument defaults to the fully qualified domain name of the local host
* SMTP.login(user, password, *, initial_response_ok=True)
Log in on an SMTP server that requires authentication. The arguments are the username and the password to authenticate with. If there has been no previous EHLO or HELO command this session, this method tries ESMTP EHLO first. This method will return normally if the authentication was successful, or may raise the following exceptions
* SMTP.starttls(keyfile=None, certfile=None, context=None)
Put the SMTP connection in TLS (Transport Layer Security) mode. All SMTP commands that follow will be encrypted. You should then call ehlo() again
* SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())
Send mail
# ALERT NOTIFICATION
* Plyer is a Python library for accessing features of your hardware / platforms.
* plyer.notification= <plyer.facades.notification.Notification object>
Notification proxy to plyer.facades.Notification
