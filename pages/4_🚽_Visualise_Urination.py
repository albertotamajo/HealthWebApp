import streamlit as st
from utils import open_binary, s3fs_file_system
from constants import AWS_BUCKET, URINATION_FILE
import pandas as pd

st.set_page_config(
    page_title="Visualise urination",
    page_icon="🚽",
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

st.write("# Visualise urination! 🚽")


st.markdown(
    """
    Visualise a history of your urinations.
    """
)
file = "{0}{1}".format(AWS_BUCKET, URINATION_FILE)
if fs.exists(file):
    l = open_binary(fs, file)
    l.reverse()
    if len(l) != 0:
        d = {"Date": [d for d,_,_ in l], "Quantity": [q for _,q,_ in l], "Urgency": [u for _, _, u in l]}
        df = pd.DataFrame(d)
        st.dataframe(df)
    else:
        st.error("Sorry, there is no entry in the file.")
else:
    st.error("Sorry, there is no file yet.")