import streamlit as st
from PIL import Image
import requests

def generate_caption():
    image_file = st.file_uploader("Upload Image", type = ['jpg','png','jpeg'])

    if image_file is None:
        st.warning("Please Upload an Image")

    if image_file is not None:
        image1 = Image.open(image_file)
        rgb_im = image1.convert('RGB')
        image = rgb_im.save("saved_image.jpg")
        image_path = "saved_image.jpg"
        st.image(image1,width = 400)

    if st.sidebar.button("Generate Caption ✒️"):
        if image_file is not None:
            r = requests.post(
                "https://api.deepai.org/api/neuraltalk",
                files={
                    'image': open('saved_image.jpg', 'rb'),
                },
                headers={'api-key': '8f0499fe-bf0f-455d-9f4b-3acb442b49c4'}
            )
            output = r.json()["output"].title()
            st.warning('Output : "{}"'.format(output))
        else:
            st.error("Please Upload Image!!!")
