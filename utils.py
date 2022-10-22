import streamlit as st
import base64
import pandas as pd
import io
from feature_engineering.email_scrap import convert_df


def download_df_as_csv(df):
    converted = convert_df(df)
    st.download_button(
        "Press to Download",
        converted,
        "emails.csv",
        "text/csv",
        key='download-csv')


def download_df_as_excel(df):
    towrite = io.BytesIO()
    downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    towrite.close()
    linko = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="myfilename.xlsx">Download excel file</a>'
    st.markdown(linko, unsafe_allow_html=True)

# def download_df_as_excel_engine(df):
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     df_xlsx = df.to_excel(writer, index=False, sheet_name='Sheet1')
#     workbook = writer.book
#     worksheet = writer.sheets['Sheet1']
#     format1 = workbook.add_format({'num_format': '0.00'})
#     worksheet.set_column('A:A', None, format1)
#     writer.save()
#     processed_data = output.getvalue()
#     st.download_button(label='📥 Press to Download',
#                        data=df_xlsx,
#                        file_name='df_test.xlsx')
#     return processed_data
