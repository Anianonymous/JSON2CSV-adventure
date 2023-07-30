import pandas as pd
import streamlit as st
json_file = st.text_input("Enter the path: ")
if json_file:
    try:
        with open(json_file, encoding='utf-8') as inputFile:
            df = pd.read_json(inputFile)
        st.write("Json file has loaded successfully")
    except FileNotFoundError:
        st.write("File not found, please make sure the file path is correct.")
locate_csv_file=st.text_input("enter the path to save CSV file : ")
if locate_csv_file:
    try:
        df.to_csv(locate_csv_file, encoding='utf-8', index=False)
        st.write("CSV file saved successfully!")
    except Exception:
        st.write("Error has occurred ",Exception)
