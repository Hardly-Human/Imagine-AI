import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np

face_cascade = cv2.CascadeClassifier('./frecog/haarcascade_frontalface_default.xml')

@st.cache
def load_image(image):
	img = Image.open(image)
	return img

@st.cache
def detect_faces(img):
	new_img = np.array(img.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
	# Detect Face
	faces = face_cascade.detectMultiScale(gray,1.3,4)
	# Draw Rectangle
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

	return img,faces

def facial_recognition():
    image_file = st.file_uploader("Upload Image",type = ['jpg','png','jpeg'])

    if image_file is not None:
        our_img = load_image(image_file)
        st.subheader('Uploaded Image')
        st.image(our_img, width = 800)
    else:
        st.warning("Please Upload an Image")

    if st.button("Process"):
        result_img,result_faces = detect_faces(our_img)
        st.subheader('Processed Image')
        st.image(result_img,width = 800)
        st.success('Found {} faces'.format(len(result_faces)))
