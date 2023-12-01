import streamlit as st


def page_summary_body():
    st.title("Lydia's Predictive App")
    st.write('### This App is for exclusive use of Lydia Doe\n'
             ' This is the dashboard for your predictive application.\n'
             " Here you'll be able to obtain information about the best prices"
             " for your properties and also you will receive an in-depth study"
             " about the most important variables to consider when deciding a"
             " final price")

    st.success("The business requirement for this project is the following:"
               "\n\nLydia Doe, has requested as a friend, to analyze and build"
               " a dashboard where she will be able to see the predicted"
               " prices for the houses she inherited in Ames, Iowa and to"
               " also be able to predict the price for any other property she"
               " might own in the area in the future.")

    st.info('The dataset used for the development of this app was publicly'
            ' available on the famous Machine Learning Platform "Kaggle".\n'
            ' The following are the descriptions of the dataset variables.')

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

    st.markdown('#### How To Use This Dashboard')
    st.info(
        'You are currently reading this text on the summary page.'
        " This page has all the information you need to navigate the contents"
        " of this app.\n\n"
        " On the left you'll find a button to toggle the sidebar."
        " Once you have accessed the sidebar you'll find a list of all the"
        " pages of this dashboard. The pages are organized like this:"
    )
    st.markdown(
        "* **Quick Project Summary:**\n\n"
        "In this page you'll be able to get an overview of the dataset"
        " and what the specific columns in the dataset mean. You will also"
        " find instructions on how to use the dashboard.\n\n"

        "* **Sale Price Correlation Study:**\n\n"
        "In this page you will find the result of the correlation studies"
        " The correlation studies will show you how different variable in the"
        " dataset correlate with the target (Sale Price). In addition to that"
        " there will also be some plots and graphs present. These will help"
        " you visualize the correlation levels.\n\n"

        "* **House Price Prediction:**\n\n"
        "In this page you will be presented with the result of the prediction"
        " for your inherited houses' sale prices. Below that you'll be also"
        " able to input the information for other houses or properties and"
        " receive the predicted price.\n\n"

        "* **Project Hypothesis:**\n\n"
        "In this page you'll find a description of the initial hypothesis"
        " and the results of the comparison between the hypothesis and the"
        " actual data we obtained after the analysis. This page might contain"
        " technical language and it could be difficult to understand. The app"
        " will still be usable even for non-technical personnel.\n\n"

        "* **ML Pipeline:**\n\n"
        "This page is strictly for technical personnel. It illustrates the"
        " Machine Learning Pipeline and the process used to achieve the"
        " desired metrics."


    )
