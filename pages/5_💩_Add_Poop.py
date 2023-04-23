import streamlit as st
import pytz
from datetime import datetime
from utils import open_binary, write_binary, s3fs_file_system
from constants import AWS_BUCKET, POOP_FILE

st.set_page_config(
    page_title="Add poop",
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

st.write("# Add poop! 💩")


st.markdown(
    """
    Record the poop you take.
    """
)
quantity_default = 200
file = "{0}{1}".format(AWS_BUCKET, POOP_FILE)

type = st.selectbox('What is the type of poop?', ["<select>", "1", "2", "3", "4", "5", "6"])
quantity = st.selectbox('How much of it did you take?', ["<select>", "X", "XX", "XXX"])
password = st.text_input('Password')
if st.button('Add poop'):
    if type == '<select>' or quantity == "<select>" or password != st.secrets["PASSWORD"]:
        if type == '<select>':
            st.error('You need to select a type of poop')
        if quantity == '<select>':
            st.error('You need to select a quantity')
        if password != st.secrets["PASSWORD"]:
            st.error('You need to type a correct password')
    else:
        datetime = datetime.now(pytz.timezone("Europe/Rome"))
        date = "{0}-{1}-{2} {3}:{4}".format(datetime.year, datetime.month, datetime.day, datetime.hour, datetime.minute)
        l = [(date, type, quantity)]
        if fs.exists(file):
            l = open_binary(fs, file) + l
        else:
            fs.touch(file)
        write_binary(fs, file, l)
        st.success('Poop added successfully!')
