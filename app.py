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

    reward, selected = st.columns([1, 2])

    if selected_column and selected_row is not None:
        with selected:
            st.write(f"**{selected_column}**")
            cell_value = df.loc[selected_row, selected_column]

            if selected_column == "traj" or selected_column == "info":
                try:
                    convo = ast.literal_eval(cell_value)
                    st.write(convo)
                except Exception as e:
                    st.write(f"Cannot display this record: {e}")

        with reward:
            st.write("**reward**")
            st.write(df["reward"][selected_row])
