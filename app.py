import ast

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
            try:
                information = ast.literal_eval(df['info'][selected_row])
                st.write(information)
            except Exception as e:
                st.write(f"Error displaying info: {e}")
                st.write(df['info'][selected_row])

        with traj:
            st.subheader("traj")
            convo_str = df['traj'][selected_row]

            try:
                display = ast.literal_eval(convo_str)
                st.write(display)

            except Exception as e:
                st.write(f"Cannot display this record cleanly. Will separate based on role: {e}")
                pieces = convo_str.split("'role':")
                st.write(pieces)

