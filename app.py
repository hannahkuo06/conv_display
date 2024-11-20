import ast
import json

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conversation Display",
                   layout="wide")

uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    st.dataframe(df)
    selected_row = st.number_input('Select a row', min_value=0, max_value=len(df)-1, step=1)

    if selected_row is not None:
        task_id, reward, trial = st.columns(3)
        with task_id:
            st.write("**task_id**")
            st.write(df["task_id"][selected_row])
        with reward:
            st.write("**reward**")
            st.write(df["reward"][selected_row])
        with trial:
            st.write("**trial**")
            st.write(df["trial"][selected_row])

        cell_value = df.loc[selected_row, "traj"]

        info, traj = st.columns([1, 2])

        with info:
            st.subheader("info")
            information = ast.literal_eval(df['info'][selected_row])
            st.write(information)

        with traj:
            st.subheader("traj")
            try:
                convo = ast.literal_eval(df['traj'][selected_row])
                st.write(convo)

            except Exception as e:
                st.write(f"Cannot display this record: {e}")
