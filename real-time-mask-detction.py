#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.models import load_model
import cv2
import numpy as np
import tkinter
import tkinter as tk
from tkinter import messagebox
import smtplib


# In[ ]:


# Iinialize Tkinter
root = tkinter.Tk()
root.withdraw()


# In[ ]:


# Load trained deep learning model
model = load_model('face-mask-image-classification-with-keras_2.h5')


# In[ ]:


# Classifier to detect face-mask
face_det_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# In[ ]:


# Capture video  for face scanning
source=cv2.VideoCapture(0)


# In[ ]:


# Dictionaries caontaing details of wearing mask and color of rectangle arund face.
# Green for wearing and Red for not wearing face mask
labels_dict={0:'MASK',1:'NO MASK'}
color_dict={0:(0,255,0),1:(0,0,255)}


# In[ ]:


SUBJECT = "Subject"
TEXT = "violeted Fece mask policy"


while(True):

    ret, img=source.read()
    grayscale_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_det_classifier.detectMultiScale(grayscale_img,1.3,5)  

    for x,y,w,h in faces:
    
        face_img=grayscale_img[y:y+w,x:x+w]
        resized = cv2.resize(face_img,(100,100))
        normalized=resized/255.0
        reshaped=np.reshape(normalized,(1,100,100,1))
        result=model.predict(reshaped)

        label=np.argmax(result,axis=1)[0]
      
        cv2.rectangle(img,(x,y),(x+w,y+h),color_dict[label],2)
        cv2.rectangle(img,(x,y-40),(x+w,y),color_dict[label],-1)
        cv2.putText(img, labels_dict[label], (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
        # If level = 1 then  it means wearing No mask and 0 means wearing mask
        if (label == 1):
            messagebox.showwarning("Access Denied")
            #%run mail.py
            #%run alert_notification.py
            
        else:
            pass
            break
    cv2.imshow('Live scanning',img)
    key=cv2.waitKey(1)
    
    if(key==27):
        break
        
cv2.destroyAllWindows()
source.release()        

