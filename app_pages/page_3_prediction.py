import streamlit as st


def page_prediction_body():
    st.markdown("## Machine Learning Prediction")
    st.write("In this page we will show the predicted prices for Lydia's"
             " properties and we will also allow Lydia to run predictions on"
             " all other properties she might own or acquire in the future.")

    st.beta_columns(st.selectbox(label='ciao',
                                 options=['bella', 'hola', 'hello']))
