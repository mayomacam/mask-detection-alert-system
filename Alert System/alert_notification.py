import datetime  # for reading present date
import time
import requests  # for retreiving coronavirus data from web
from plyer import notification  # for getting notification on your PC


condition = 1  # for testing the notification only
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        #creating icon for the notification
        #we need to give adress of icon file(in ico file format)
        app_icon="C:\\Users\\Anurag Kumar\\Desktop\\icon.ico",
        # the notification stays for 50sec
        timeout=15
    )

#if we detect person without mask
if (condition):
    notifyMe("Mask Detection Alert!","Someone is without mask")
