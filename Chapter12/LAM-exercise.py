import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl

mpl.use("pdf")

#find face and eyes
face_cascade = cv2.CascadeClassifier('/home/jovyan/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/jovyan/data/haarcascade_eye.xml')
#img = cv2.imread('../../images/lam.png')
#img = cv2.imread('./mikkel.png')
img = cv2.imread('./eyesGroup.jpeg')

cv2.imwrite('./lam_copy.png', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('./lam_copy.png_greyscale.png', gray)

faces = face_cascade.detectMultiScale(gray)
print(faces)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print(eyes)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imwrite("./lam_final.png", img)
