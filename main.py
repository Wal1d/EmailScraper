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

        col1, col2 = st.columns(2)

        with col1:
            list_links = upload_file_st()

        with col2:
            text_input = st.text_input(
                "Enter some link 👇",
            )
            list_links_from_str = text_input.strip().split(',')
            st.write(f"List of links : {list_links_from_str}")

        clicked = st.button('Start')
        if clicked and (list_links or list_links_from_str):
            with st.spinner('Loading DATA'):
                list_of_emails = []
                if list_links :
                    list_of_emails = main_scrap(list_links)
                if list_links_from_str:
                    list_of_emails = main_scrap(list_links_from_str)

            print(f"list_of_emails ==== {list_of_emails}")
            #if list_of_emails:
            for email in list_of_emails:
               st.write(email)
            st.balloons()


if __name__ == '__main__':
    main()
