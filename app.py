import streamlit as st

from app_pages.page_1_summary import page_summary_body

with st.sidebar:
    add_checkbox = st.checkbox('Page 1')

page_summary_body()