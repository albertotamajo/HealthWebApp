import streamlit as st
import pytz
from datetime import datetime
from utils import open_binary, write_binary, s3fs_file_system
from constants import AWS_BUCKET, LIQUIDS_FILE

st.set_page_config(
    page_title="Add liquids",
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

st.write("# Add liquids! 🥤")


st.markdown(
    """
    Record the liquids you have just drunk.
    """
)
quantity_default = 200
file = "{0}{1}".format(AWS_BUCKET, LIQUIDS_FILE)

type = st.selectbox('What is the liquid?', ["<select>", "Water", "Milk", "Others"])
quantity = st.number_input('How much of it have you drunk (ml)?', min_value=0, max_value=1000, value=quantity_default, step=1)
password = st.text_input('Password')
if st.button('Add liquids'):
    if type == '<select>' or password != st.secrets["PASSWORD"]:
        if type == '<select>':
            st.error('You need to select a type of liquid')
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
        st.success('Liquid added successfully!')
