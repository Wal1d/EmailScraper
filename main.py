import streamlit as st

from feature_engineering.email_scrap import main_scrap
from upload_file import upload_file_st
from utils import download_df_as_csv, download_df_as_excel

st.title('Tiny ML in nature')


def main():
    menu = ["Home", "Scrap from list", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    list_links = []
    if choice == "Home":
        st.subheader("HomePage")

        list_links = upload_file_st()
        clicked = st.button('Start')

        if clicked and list_links:
            with st.spinner('Loading DATA'):
                list_of_emails = []
                if list_links:
                    list_of_emails = main_scrap(list_links)
                    print(f"list_of_emails ==== {list_of_emails}")
                    download_df_as_excel(list_of_emails)


    if choice == "Scrap from list":

        text_input = st.text_input(
            "Enter some link 👇",
        )
        list_links_from_str = text_input.strip().split(',')
        st.write(f"List of links : {list_links_from_str}")

        clicked = st.button('Start')

        if clicked and list_links_from_str:
            with st.spinner('Loading DATA'):
                list_of_emails = []
                if list_links_from_str:
                    list_of_emails = main_scrap(list_links_from_str)
                    download_df_as_excel(list_of_emails)


if __name__ == '__main__':
    main()
