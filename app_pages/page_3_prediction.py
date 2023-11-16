import streamlit as st
import numpy as np
import pandas as pd
import joblib


def page_prediction_body():
    st.markdown("## Machine Learning Prediction")
    st.write("In this page we will show the predicted prices for Lydia's"
             " properties and we will also allow Lydia to run predictions on"
             " all other properties she might own or acquire in the future.")
    st.write('---')
    st.write('The following is an overview of the dataset. At the top you will'
             " find the name of the columns with the respective values.")
    df = pd.read_csv(
        'outputs/dataset/collection/clean_dataset.csv')
    st.dataframe(data=df)

    st.markdown("### This is the data frame with the data from the inherited"
                " houses. We will show the predicted prices for the houses"
                " below")
    df_new_houses = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001"
        "/house-price/inherited_houses.csv")
    st.dataframe(data=df_new_houses)

    # Now I will load the regression pipeline and predict the prices
    regression_pipeline = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/regressor_pipeline.pkl")
    # create two columns to display the buttons which will give access to 
    # the prediction for the prices and all the widgets to run predictions
    # on future houses
    inherited_houses_col, future_predict = st.beta_columns(2)
    with inherited_houses_col:
        if st.button(label='Show Predicted Prices'):
            predicted_prices = regression_pipeline.predict(df_new_houses)
            predicted_prices = pd.Series(predicted_prices).astype(int)

            st.write(predicted_prices)

    # This df is where I will store the inputs from the widgets
    X_live = pd.DataFrame()

    # All the input widgets necessary to fit the data to the ML pipeline.
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    col9, col10, col11, col12 = st.beta_columns(4)
    col13, col14, col15, col16 = st.beta_columns(4)
    col17, col18, col19, col20 = st.beta_columns(4)
    col21, col22, col23 = st.beta_columns(3)
    with future_predict:
        if st.button('Access Input Interface'):
            with col1:
                feature = '1stFlrSF'
                st.number_input(
                    label="1st Floor Square Feet",
                    value=int(df_new_houses[feature].median()),
                    format='%d'
                )

            with col2:
                feature = '2ndFlrSF'
                st.number_input(
                    label="2nd Floor Square Feet",
                    value=float(df_new_houses[feature].median()),
                    format='%f'
                )

            with col3:
                feature = 'BedroomAbvGr'
                st.number_input(
                    label="Bedrooms Above Grade (not Basement)",
                    value=0.0,
                    format='%f'
                )

            with col4:
                feature = 'BsmtExposure'
                st.selectbox(
                    label="Basement Exposure",
                    options=df[feature].unique()

                )

            with col5:
                feature = 'BsmtFinSF1'
                st.number_input(
                    label='Type 1 finished square feet',
                    value=int(df_new_houses[feature].median()),
                    format='%d'
                )

            with col6:
                feature = 'BsmtFinType1'
                st.selectbox(
                    label='Rating of basement finished area',
                    options=df[feature].unique()
                )

            with col7:
                feature = 'BsmtUnfSF'
                st.number_input(
                    label='Unfinished square ft. of basement area',
                    value=int(df[feature].median()),
                    format='%d'
                )

            with col8:
                feature = 'EnclosedPorch'
                st.number_input(
                    label='Enclosed Porch area in sq. ft.',
                    value=df[feature].median()
                )

            with col9:
                feature = 'GarageArea'
                st.number_input(
                    label='Square Feet of Garage',
                    value=int(df[feature].median()),
                    format='%d'
                )

            with col10:
                feature = 'GarageFinish'
                st.selectbox(
                    label='State of the Garage',
                    options=['RFn', 'Unf', 'Fin', 'None']
                )

            with col11:
                feature = 'GarageYrBlt'
                st.number_input(
                    label='Year of garage construction',
                    min_value=1850,
                    max_value=2024,
                    value=1994,
                    format='%d'
                )

            with col12:
                feature = 'GrLivArea'
                st.number_input(
                    label='Sq. ft. of living area above ground',
                    min_value=0,
                    max_value=5000,
                    value=int(df[feature].median())
                )

            with col13:
                feature = 'KitchenQual'
                st.selectbox(
                    label='Quality of the Kitchen',
                    options=df[feature].unique()
                )

            with col14:
                feature = 'LotArea'
                st.number_input(
                    label='Lot size in Sq ft.',
                    min_value=1000,
                    max_value=200000,
                    format='%d',
                    value=25000
                )

            with col15:
                feature = 'LotFrontage'
                st.number_input(
                    label='Feet of street adjacent to the property',
                    min_value=1,
                    max_value=10000
                )

            with col16:
                feature = 'MasVnrArea'
                st.number_input(
                    label='Masonry veneer area in square feet',
                    min_value=0,
                    max_value=20000
                )

            with col17:
                feature = 'OpenPorchSF'
                st.number_input(
                    label='Sq ft of open porch',
                    min_value=0,
                    max_value=15000
                )

            with col18:
                feature = 'OverallCond'
                st.selectbox(
                    label='Overall Conditions (1-10)',
                    options=np.arange(1, 11)
                )

            with col19:
                feature = 'OverallQual'
                st.selectbox(
                    label='Overall Quality of the house (1 to 10)',
                    options=np.arange(1, 11)
                )

            with col20:
                feature = 'TotalBsmtSF'
                st.number_input(
                    label='Sq ft of the basement',
                    min_value=0,
                    max_value=20000,
                    value=1000,
                    format='%d'
                )

            with col21:
                feature = 'WoodDeckSF'
                st.number_input(
                    label='Sq ft of the wood deck',
                    min_value=10,
                    max_value=20000,
                    value=500
                )

            with col22:
                feature = 'YearBuilt'
                st.selectbox(
                    label='Year of construction',
                    options=np.arange(1800, 2025)
                )

            with col23:
                feature = 'YearRemodAdd'
                st.selectbox(
                    label='Year of remodeling (same as construction'
                          'if no remodeling)',
                    options=np.arange(1800, 2025)
                )

# Aggiungi il codice per metter tutti gli input nel X_live df
# Aggiungi un pulsante per fare la predizione sui nuovi dati
