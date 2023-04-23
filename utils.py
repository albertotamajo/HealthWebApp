import streamlit as st
import s3fs
import pickle


@st.cache_resource
def s3fs_file_system():
    return s3fs.S3FileSystem(anon=False)


def open_binary(fs, file):
    with fs.open(file, 'rb') as f:
        data = pickle.load(f)
    return data


def write_binary(fs, file, data):
    with fs.open(file, 'wb') as f:
        pickle.dump(data, f)