import ast
import streamlit as st
import pandas as pd

st.title("Conversation Display")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])
#
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    st.dataframe(df)
    # Allow the user to select a column from the DataFrame
    selected_column = st.selectbox('Select a column', df.columns)

    # Allow the user to select a row (index) from the DataFrame
    selected_row = st.number_input('Select a row', min_value=0, max_value=len(df)-1, step=1)

    # Display the selected cell content
    if selected_column and selected_row is not None:
        cell_value = df.loc[selected_row, selected_column]
        try:
            convo = ast.literal_eval(df[selected_column][selected_row])
            st.write(convo)
        except Exception as e:
            st.write(f"Cannot display this record: {e}")
