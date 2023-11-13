import streamlit as st
import pandas as pd

# This function contains the content of the page. It will be called in the
# app.py file


def page_correlation_body():
    st.title('Correlation Study')
    st.info("This page will illustrate the correlation study and the most"
            " significant variables correlated with the Sale Price.")
    st.markdown("### What is a correlation?")
    st.write("A correlation happens when for a given value change another"
             "value changes as well. Correlation can be positive which means"
             " that when one value increases the other increases as well, or"
             " it can be negative, which means that if a given value increases"
             " the other value descreases. The correlation levels are"
             " described"
             " on a continuous value from -1 to 1. When the value is either -1"
             " or 1, then we know the correlation is perfect. Obviously -1"
             " would be a perfect negative correlation while 1 is a perfect"
             " positive. It is important to note that correlation doesn't"
             " mean causation so we should always indulge in more"
             " investigation after drawing some conclusions. Especially from"
             " the correlation of just 1 variable against another.")
    st.markdown("#### Spearman Correlation")

    # This segment of code load shows the one hot encoded dataset. (10 samples)
    df_ohe = pd.read_csv(
        '/workspaces/Fabrizio-Project-Five/outputs/'
        'dataset/collection/feature_engineered_dataset.csv'
    )
    if st.checkbox('Dataset'):
        st.write('These are 10 rows from the pre-processed dataset')
        st.write(df_ohe.head(10))
    
    # this section shows the sperman correlation
    


