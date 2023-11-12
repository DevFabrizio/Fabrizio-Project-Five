import streamlit as st


def page_summary_body():
    st.title("Lydia's Predictive App")
    st.write('### This App is for exclusive use of Lydia Doe\n'
             'This is the dashboard for your predictive application.\n'
             "Here you'll be able to obtain information about the best prices"
             "for your properties and also you will receive an in-depth study"
             "about the most important variables to consider when deciding a"
             "final price")

    st.info('The dataset used for the development of this app was publicly'
            'available on the famous Machine Learning Platform "Kaggle".\n'
            'The following are the descriptions of the dataset variables.')

    if st.checkbox('Dataset Details'):
        st.write(
            '| 1stFlrSF | First Floor square feet |\n\n'
            '| 2ndFlrSF | Second floor square feet |\n\n'
            '| BedroomAbvGr | Bedrooms above grade'
            ' (not including basement) |\n\n'
            '| BsmtExposure | Basement Exposure |\n\n'
            '| BsmtFinType1 | Basement Finished Area Rating |\n\n'
            '| BsmtFinSF1 | Type 1 finished square feet |\n\n'
            '| BsmtUnfSF | Unfinished square feet of basement area |\n\n'
            '| TotalBsmtSF | Total square feet of basement area |\n\n'
            '| GarageArea | Size of garage in square feet |\n\n'
            '| GarageFinish | Interior finish of the garage |\n\n'
            '| GarageYrBlt | Year garage was built |\n\n'
            '| GrLivArea | Above grade (ground)'
            ' living area square feet |\n\n'
            '| KitchenQual | Kitchen quality |\n\n'
            '| LotArea | Lot size in square feet |\n\n'
            '| LotFrontage | Linear feet of street'
            ' connected to property |\n\n'
            '| MasVnrArea | Masonry veneer area in square feet |\n\n'
            '| EnclosedPorch | Enclosed porch area in square feet |\n\n'
            '| OpenPorchSF | Open porch area in square feet |\n\n'
            '| OverallCond | Rates the overall condition of'
            ' the house |\n\n'
            '| OverallQual | Rates the overall material'
            ' and finish of the house |\n\n'
            '| WoodDeckSF | Wood deck area in square feet |\n\n'
            '| YearBuilt | Original construction date |\n\n'
            '| YearRemodAdd | Remodel date (same as construction date if'
            ' no remodeling or additions) |\n\n'
            '| SalePrice | Sale Price |')
