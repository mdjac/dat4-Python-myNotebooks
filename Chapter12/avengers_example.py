import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl

#Example with avengers
mpl.use("pdf")
face_cascade = cv2.CascadeClassifier('/home/jovyan/data/haarcascade_frontalface_default.xml')
print(type(face_cascade))
img = cv2.imread('../../images/avengers.jpg')
cv2.imwrite('./avengers_copy.jpg', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
figure = plt.figure(figsize = (100,20))
plt.imsave('./avengers_faces_after.jpg', img)
final_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imsave("./avengers_faces_final.jpg", final_img)