import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.write("# Welcome to the Health Management Web App! 👋")

st.sidebar.success("Select one of these functionalities.")

st.markdown(
    """
    This web app is used by Alberto Tamajo.
"""
)