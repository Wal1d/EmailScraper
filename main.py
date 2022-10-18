import streamlit as st

from feature_engineering.email_scrap import main_scrap
from upload_file import upload_file_st

st.title('Tiny ML in nature')


def main():
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    list_links = []
    if choice == "Home":
        st.subheader("HomePage")
        list_links = upload_file_st()
        clicked = st.button('Start')
        if clicked and list_links:
            with st.spinner('Loading DATA'):
                list_of_emails = main_scrap(list_links)
                if list_of_emails:
                    st.write(list_of_emails)


if __name__ == '__main__':
    main()
