import urllib.request
import streamlit as st

from facial_recognition import facial_recognition
from image_colorization import image_colorization
from style_transfer import style_transfer
from toonify_image import toonify_image
from image_captioning import generate_caption

def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/Hardly-Human/Imagine-AI/main/app/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")


#####################################
# Sidebar options
#####################################
SIDEBAR_OPTION_PROJECT_INFO = "Show Project Info"
SIDEBAR_OPTION_IMAGE_PLAYGROUND = "Image Playground"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO,SIDEBAR_OPTION_IMAGE_PLAYGROUND]


#####################################
# sidebar Tasks
#####################################
SIDEBAR_TASK_FACIAL_RECOGNITION = "Facial Recognition"
SIDEBAR_TASK_IMAGE_COLORIZATION = "Image Colorization"
SIDEBAR_TASK_STYLE_TRANSFER = "Neural Style Transfer"
SIDEBAR_TASK_TOONIFY_IMAGE = "Toonify Image"
SIDEBAR_TASK_IMAGE_CAPTIONING = "Image Captioning"

SIDEBAR_TASKS = [SIDEBAR_TASK_FACIAL_RECOGNITION, SIDEBAR_TASK_IMAGE_COLORIZATION, SIDEBAR_TASK_STYLE_TRANSFER, SIDEBAR_TASK_TOONIFY_IMAGE, SIDEBAR_TASK_IMAGE_CAPTIONING]

#####################################
# main
#####################################

def main():
    st.sidebar.warning('\
        For Best results, Please upload SINGLE-person images')
    st.sidebar.write(" ------ ")
    st.sidebar.title("Explore the Following")

    st.title("Welcome to Imagine AI")

    app_mode = st.sidebar.selectbox("Please select from the following", SIDEBAR_OPTIONS)

    if(app_mode == SIDEBAR_OPTION_PROJECT_INFO):
        st.sidebar.write(" ------ ")
        st.sidebar.success("Project information showing on the right!")
        st.write(get_file_content_as_string("project-info.md"))

    elif(app_mode == SIDEBAR_OPTION_IMAGE_PLAYGROUND):
        task = st.sidebar.selectbox("Please select a Task", SIDEBAR_TASKS)

        if (task == SIDEBAR_TASK_FACIAL_RECOGNITION):
            st.header(SIDEBAR_TASK_FACIAL_RECOGNITION)
            facial_recognition()
        elif(task == SIDEBAR_TASK_IMAGE_COLORIZATION):
            st.header(SIDEBAR_TASK_IMAGE_COLORIZATION)
            image_colorization()
        elif (task == SIDEBAR_TASK_STYLE_TRANSFER):
            st.header(SIDEBAR_TASK_STYLE_TRANSFER)
            style_transfer()
        elif(task == SIDEBAR_TASK_TOONIFY_IMAGE):
            st.header(SIDEBAR_TASK_TOONIFY_IMAGE)
            toonify_image()
        elif(task == SIDEBAR_TASK_IMAGE_CAPTIONING):
            st.header(SIDEBAR_TASK_IMAGE_CAPTIONING)
            generate_caption()





if __name__=="__main__":
    main()
