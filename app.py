import streamlit as st
# list of import for the pages of the app
from app_pages import (
    page_1_summary,
    page_2_correlation,
    page_3_prediction,
    page_4_hypothesis,
    page_5_pipeline
)


def main():
    """
    This function will run the app by creating a sidebar and based on the
    user's choice it will call the main function from that specific page and
    display the contents of the page on the dashboard.
    """
    # creation of the sidebar in the dashboard with list of the pages
    page = st.sidebar.radio("Choose a page", ["Quick Project Summary",
                                              "Sale Price Correlation Study",
                                              "House Price Prediction",
                                              "Project Hypothesis",
                                              "ML Pipeline"])

    if page == "Quick Project Summary":
        page_1_summary.page_summary_body()
    elif page == "Sale Price Correlation Study":
        page_2_correlation.page_correlation_body()
    elif page == "House Price Prediction":
        page_3_prediction.page_prediction_body()
    elif page == "Project Hypothesis":
        page_4_hypothesis.page_hypothesis_body()
    elif page == "ML Pipeline":
        page_5_pipeline.page_pipeline_body()

# this logic will allow the app to be ran when calling the "streamlit run
# app.py" function


if __name__ == "__main__":
    main()
