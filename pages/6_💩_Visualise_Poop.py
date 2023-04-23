import streamlit as st
from utils import open_binary, s3fs_file_system
from constants import AWS_BUCKET, POOP_FILE
import pandas as pd

st.set_page_config(
    page_title="Visualise poop",
    page_icon="💩",
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

st.write("# Visualise poop! 💩")


st.markdown(
    """
    Visualise a history of your poop.
    """
)
file = "{0}{1}".format(AWS_BUCKET, POOP_FILE)
if fs.exists(file):
    l = open_binary(fs, file)
    l.reverse()
    if len(l) != 0:
        d = {"Date": [d for d,_,_ in l], "Type": [t for _,t,_ in l], "Quantity": [q for _, _, q in l]}
        df = pd.DataFrame(d)
        st.dataframe(df)
    else:
        st.error("Sorry, there is no entry in the file.")
else:
    st.error("Sorry, there is no file yet.")