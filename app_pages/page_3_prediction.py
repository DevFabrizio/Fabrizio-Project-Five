import streamlit as st
import numpy as np
import pandas as pd
import joblib


def page_prediction_body():
    st.title('Machine Learning Prediction')
    st.write("In this page we will show the predicted prices for Lydia's"
             " properties and we will also allow Lydia to run predictions on"
             " all other properties she might own or acquire in the future.")
    st.write('---')
    st.write('The following is an overview of the dataset. At the top you will'
             " find the name of the columns with the respective values.")
    df = pd.read_csv(
        'outputs/dataset/collection/clean_dataset.csv')
    st.dataframe(data=df)
    st.write('---')

    st.markdown("### This is the data frame with the data from the inherited"
                " houses. We will show the predicted prices for the houses"
                " below")
    df_new_houses = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001"
        "/house-price/inherited_houses.csv")
    st.dataframe(data=df_new_houses)
    st.write('---')

    # Now I will load the regression pipeline and predict the prices
    regression_pipeline = joblib.load(
        "outputs/ml_pipeline/predict_saleprice/regressor_pipeline.pkl")

    if st.button(label='Show Predicted Prices'):
        predicted_prices = regression_pipeline.predict(df_new_houses)
        predicted_prices = pd.Series(predicted_prices).astype(int)

        st.write(predicted_prices)

    # This df is where I will store the inputs from the widgets
    X_live = pd.DataFrame([], index=[0])

    # widgets interface introduction
    st.markdown('## Predictive Interface')
    st.write("In this series of widgets you will be able to plug in your data"
             " from any other house or property you might possess and run the "
             "machine learning algorithm to get an instant price. If any of"
             " inputs might be confusing I suggest you to reference the "
             "explaination table in page 1.")
    st.write('---')

    # All the input widgets necessary to fit the data to the ML pipeline.
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    col9, col10, col11, col12 = st.beta_columns(4)
    col13, col14, col15, col16 = st.beta_columns(4)
    col17, col18, col19, col20 = st.beta_columns(4)
    col21, col22, col23 = st.beta_columns(3)

    # series of input widgets
    with col1:
        feature = '1stFlrSF'
        widget = st.number_input(
            label="1st Floor Square Feet",
            value=int(df_new_houses[feature].median()),
            format='%d'
        )
    X_live[feature] = widget

    with col2:
        feature = '2ndFlrSF'
        widget = st.number_input(
            label="2nd Floor Square Feet",
            value=float(df_new_houses[feature].median()),
            format='%f'
        )
    X_live[feature] = widget

    with col3:
        feature = 'BedroomAbvGr'
        widget = st.number_input(
            label="Bedrooms Above Grade (not Basement)",
            value=0.0,
            format='%f'
        )
    X_live[feature] = widget

    with col4:
        feature = 'BsmtExposure'
        widget = st.selectbox(
            label="Basement Exposure",
            options=df[feature].unique()
        )
    X_live[feature] = widget

    with col5:
        feature = 'BsmtFinSF1'
        widget = st.number_input(
            label='Type 1 finished square feet',
            value=int(df_new_houses[feature].median()),
            format='%d'
        )
    X_live[feature] = widget

    with col6:
        feature = 'BsmtFinType1'
        widget = st.selectbox(
            label='Rating of basement finished area',
            options=df[feature].unique()
        )
    X_live[feature] = widget

    with col7:
        feature = 'BsmtUnfSF'
        widget = st.number_input(
            label='Unfinished square ft. of basement area',
            value=int(df[feature].median()),
            format='%d'
        )
    X_live[feature] = widget

    with col8:
        feature = 'EnclosedPorch'
        widget = st.number_input(
            label='Enclosed Porch area in sq. ft.',
            value=df[feature].median()
        )
    X_live[feature] = widget

    with col9:
        feature = 'GarageArea'
        widget = st.number_input(
            label='Square Feet of Garage',
            value=int(df[feature].median()),
            format='%d'
        )
    X_live[feature] = widget

    with col10:
        feature = 'GarageFinish'
        widget = st.selectbox(
            label='State of the Garage',
            options=['RFn', 'Unf', 'Fin', 'None']
        )
    X_live[feature] = widget

    with col11:
        feature = 'GarageYrBlt'
        widget = st.number_input(
            label='Year of garage construction',
            min_value=1850,
            max_value=2024,
            value=1994,
            format='%d'
        )
    X_live[feature] = widget

    with col12:
        feature = 'GrLivArea'
        widget = st.number_input(
            label='Sq. ft. of living area above ground',
            min_value=0,
            max_value=5000,
            value=int(df[feature].median())
        )
    X_live[feature] = widget

    with col13:
        feature = 'KitchenQual'
        widget = st.selectbox(
            label='Quality of the Kitchen',
            options=df[feature].unique()
        )
    X_live[feature] = widget

    with col14:
        feature = 'LotArea'
        widget = st.number_input(
            label='Lot size in Sq ft.',
            min_value=1000,
            max_value=200000,
            format='%d',
            value=25000
        )
    X_live[feature] = widget

    with col15:
        feature = 'LotFrontage'
        widget = st.number_input(
            label='Feet of street adjacent to the property',
            min_value=1,
            max_value=10000
        )
    X_live[feature] = widget

    with col16:
        feature = 'MasVnrArea'
        widget = st.number_input(
            label='Masonry veneer area in square feet',
            min_value=0,
            max_value=20000
        )
    X_live[feature] = widget

    with col17:
        feature = 'OpenPorchSF'
        widget = st.number_input(
            label='Sq ft of open porch',
            min_value=0,
            max_value=15000
        )
    X_live[feature] = widget

    with col18:
        feature = 'OverallCond'
        widget = st.selectbox(
            label='Overall Conditions (1-10)',
            options=np.arange(1, 11)
        )
    X_live[feature] = widget

    with col19:
        feature = 'OverallQual'
        widget = st.selectbox(
            label='Overall Quality of the house (1 to 10)',
            options=np.arange(1, 11)
        )
    X_live[feature] = widget

    with col20:
        feature = 'TotalBsmtSF'
        widget = st.number_input(
            label='Sq ft of the basement',
            min_value=0,
            max_value=20000,
            value=1000,
            format='%d'
        )
    X_live[feature] = widget

    with col21:
        feature = 'WoodDeckSF'
        widget = st.number_input(
            label='Sq ft of the wood deck',
            min_value=10,
            max_value=20000,
            value=500
        )
    X_live[feature] = widget

    with col22:
        feature = 'YearBuilt'
        widget = st.selectbox(
            label='Year of construction',
            options=np.arange(1800, 2025)
        )
    X_live[feature] = widget

    with col23:
        feature = 'YearRemodAdd'
        widget = st.selectbox(
            label='Year of remodeling (same as construction'
                  'if no remodeling)',
            options=np.arange(1800, 2025)
        )
    X_live[feature] = widget

    if st.button('Show Live Data'):
        st.write(X_live)
    if st.button('Predict Price'):
        live_prediction = regression_pipeline.predict(X_live)
        st.write(int(live_prediction))
