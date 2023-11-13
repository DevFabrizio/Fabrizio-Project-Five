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
    st.write('We are going to show correlation with the Spearman method'
             "This is just one of the available methods we have to calculate"
             "correlations between two variables.")
    if st.checkbox('Show correlation'):
        df_ohe_corr_spearman = (df_ohe
                                .corr(method='spearman')['SalePrice']
                                .sort_values(key=abs, ascending=False)[1:]
                                .head(10))
        st.write(df_ohe_corr_spearman)
        st.write("Now that we know our most correlated features we can" 
                 "say that:\n\n"

                 "- The price of a house increases with the increase of" 
                 " Overall Quality\n"
                 "- The price of a house increases with the increase of Ground" 
                 " Living Area (in square feet) when above grade\n"
                 "- The price of a house increases when the year of" 
                 " construction is more recent\n"
                 "- The price of a house increases with the increase of" 
                 " Garage Area\n"
                 "- The price of a house increases when the Kitchen Quality is"
                 " NOT assesed as Typical/Average\n"
                 "- The price of a house increases when the year of" 
                 " construction of the garage is more recent\n"
                 "- The price of a house increases when the basement surface"
                 " (measured in square feet) increases\n"
                 "- The price of a house increases when the year of" 
                 " remodelling is more recent\n"
                 "- The price of a house increases when the surface area of" 
                 " the 1st floor (measured in square feet) increases\n"
                 "- The price of a house increases when the state of the"
                 " garage is NOT unfinished\n")

    st.markdown('#### Correlation Plots')
    if st.checkbox('Heatmap'):
        st.write("This image shows how the different variables are correlated"
                 " together. In order to read it you need to take note of the"
                 " sidebar. On it you'll find the colors mapped to the levels"
                 " of the correlation. As I previously mentioned, the closer"
                 " the value is to -1 or 1 the better is the correlation.")
        st.image(
                "/workspaces/Fabrizio-Project-Five/outputs"
                "/images/corr_heatmap.png", width=1200)
    