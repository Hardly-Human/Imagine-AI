import os
import streamlit as st

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

    st.title("Imagine AI")

    app_mode = st.sidebar.selectbox("Please select from the following", SIDEBAR_OPTIONS)


if __name__=="__main__":
    main()
