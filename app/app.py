import urllib.request
import streamlit as st

def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/Hardly-Human/Imagine-AI/main/app/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")



#####################################
# main
#####################################

SIDEBAR_OPTION_PROJECT_INFO = "Show Project Info"
SIDEBAR_OPTION_IMAGE_PLAYGROUND = "Image Playground"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_INFO,SIDEBAR_OPTION_IMAGE_PLAYGROUND]


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


if __name__=="__main__":
    main()
