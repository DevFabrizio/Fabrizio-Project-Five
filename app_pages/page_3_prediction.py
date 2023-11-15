import streamlit as st
import pandas as pd
import joblib
from feature_engine.encoding import OneHotEncoder


def page_prediction_body():
    st.markdown("## Machine Learning Prediction")
    st.write("In this page we will show the predicted prices for Lydia's"
             " properties and we will also allow Lydia to run predictions on"
             " all other properties she might own or acquire in the future.")
    st.write('---')
    st.write('The following is an overview of the dataset. At the top you will'
             " find the name of the columns with the respective values.")
    df = pd.read_csv(
        'outputs/dataset/collection/feature_engineered_dataset.csv')
    st.dataframe(data=df)

    st.markdown("### This is the data frame with the data from the inherited"
                " houses. We will show the predicted prices for the houses"
                " below")
    df_new_houses = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001"
        "/house-price/inherited_houses.csv")
    st.dataframe(data=df_new_houses)

    # Here I will one hot encode the categorical vars for the new df
    categorical_cols = []

    for col in df_new_houses.columns:
        if df_new_houses[col].dtype == 'object':
            categorical_cols.append(col)
    categorical_cols
    encoder = OneHotEncoder(variables=categorical_cols, drop_last=False)
    df_new_houses_ohe = encoder.fit_transform(df_new_houses)

    # Now I will load the regression pipeline and predict the prices
    regression_pipeline = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/regressor_pipeline.pkl")
    
    if st.button(label='Show Predicted Prices'):
        predicted_prices = regression_pipeline.predict(df_new_houses)
        st.write(predicted_prices)
