import streamlit as st
from utils import open_binary, s3fs_file_system
from constants import AWS_BUCKET, LIQUIDS_FILE
import pandas as pd

st.set_page_config(
    page_title="Visualise liquids",
    page_icon="🥤",
)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


fs = s3fs_file_system()
fs.clear_instance_cache()

st.write("# Visualise liquids! 🥤")


st.markdown(
    """
    Visualise a history of the liquids you have drunk so far.
    """
)
file = "{0}{1}".format(AWS_BUCKET, LIQUIDS_FILE)
if fs.exists(file):
    l = open_binary(fs, file)
    if len(l) != 0:
        d = {"Date": [d for d,_,_ in l], "Liquid": [i for _,i,_ in l], "Quantity (ml)": [q for _, _, q in l]}
        df = pd.DataFrame(d)
        st.dataframe(df)
    else:
        st.error("Sorry, there is no entry in the file.")
else:
    st.error("Sorry, there is no file yet.")
