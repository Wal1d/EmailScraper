import streamlit as st
import abc
import pandas as pd
import csv


class IFileManager:
    @staticmethod
    @abc.abstractmethod
    def get_csv(self, path):
        """Retrieve data from the input source
          and return an object.
        """
        return


class LocalFileManager(IFileManager):
    @staticmethod
    def get_csv(path):
        with open(path, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            rows = list(reader)
            return [row[0] for row in rows]


class STFileManager(IFileManager):
    @staticmethod
    def get_csv(uploaded_file):
        with st.spinner('Loading DATA'):
            data = pd.read_csv(uploaded_file, delimiter=';')
            data = data.iloc[:, 0]
            st.dataframe(data)
            data_list = data.values.tolist()
            return data_list



def upload_file_st():
    uploaded_file = st.file_uploader("Choose a file", type={"csv", "txt"})
    if uploaded_file is not None:
        try :
            return STFileManager.get_csv(uploaded_file)
        except Exception as err:
            st.write(f"error {err}")


