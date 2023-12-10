import streamlit as st
import numpy as np
import pandas as pd
import joblib


def page_prediction_body():
    st.title('Machine Learning Prediction')
    st.write('---')
    st.success("### **The Machine Learning Pipeline is able to predict house"
               " prices.**")
    st.write("---")
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
        "outputs/ml_pipeline/predict_saleprice/v1/regressor_pipeline.pkl")

    if st.button(label='Show Predicted Prices'):
        most_important_features = [
            'OverallQual',
            'GrLivArea',
            'KitchenQual',
            'TotalBsmtSF',
            'GarageArea'
        ]
        df_new_houses = df_new_houses.filter(most_important_features)
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
    col1, col2, col3 = st.beta_columns(3)
    col4, col5 = st.beta_columns(2)

    # series of input widgets

    with col1:
        feature = 'GarageArea'
        widget = st.number_input(
            label='Square Feet of Garage',
            min_value=0,
            value=int(df[feature].median()),
            format='%d'
        )
    X_live[feature] = widget

    with col2:
        feature = 'GrLivArea'
        widget = st.number_input(
            label='Sq. ft. of living area above ground',
            min_value=0,
            max_value=5000,
            value=int(df[feature].median())
        )
    X_live[feature] = widget

    with col3:
        # this widget maps the acronyms in the dataset to their value using
        # an object
        options = {
            'Good': 'Gd',
            'Typical/Average': 'TA',
            'Excellent': 'Ex',
            'Fair': 'Fa'
        }
        feature = 'KitchenQual'
        widget = st.selectbox(
            label='Quality of the Kitchen',
            options=options
        )
    X_live[feature] = options[widget]

    with col4:
        feature = 'OverallQual'
        widget = st.selectbox(
            label='Overall Quality of the house (1 to 10)',
            options=np.arange(1, 11)
        )
    X_live[feature] = widget

    with col5:
        feature = 'TotalBsmtSF'
        widget = st.number_input(
            label='Sq ft of the basement',
            min_value=0,
            max_value=20000,
            value=1000,
            format='%d'
        )
    X_live[feature] = widget

    if st.button('Show Live Data'):
        st.write(X_live)
    if st.button('Predict Price'):
        live_prediction = regression_pipeline.predict(X_live)
        st.write(int(live_prediction))
