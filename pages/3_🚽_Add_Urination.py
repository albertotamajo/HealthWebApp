import streamlit as st
import pytz
from datetime import datetime
from utils import open_binary, write_binary, s3fs_file_system
from constants import AWS_BUCKET, URINATION_FILE

st.set_page_config(
    page_title="Add urination",
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

st.write("# Add urination! 🚽")


st.markdown(
    """
    Record your urination details.
    """
)
quantity_default = 150
file = "{0}{1}".format(AWS_BUCKET, URINATION_FILE)

quantity = st.number_input('How much have you peed (ml)?', min_value=0, max_value=1000, value=quantity_default, step=1)
urgency = st.selectbox("What was the urgency?", ["<select>", "X", "XX", "XXX"])
password = st.text_input('Password')
if st.button('Add urination'):
    if urgency == '<select>' or password != st.secrets["PASSWORD"]:
        if type == '<select>':
            st.error('You need to select a urgency type')
        if password != st.secrets["PASSWORD"]:
            st.error('You need to type a correct password')
    else:
        datetime = datetime.now(pytz.timezone("Europe/Rome"))
        date = "{0}-{1}-{2} {3}:{4}".format(datetime.year, datetime.month, datetime.day, datetime.hour, datetime.minute)
        l = [(date, quantity, urgency)]
        if fs.exists(file):
            l = open_binary(fs, file) + l
        else:
            fs.touch(file)
        write_binary(fs, file, l)
        st.success('Urination added successfully!')