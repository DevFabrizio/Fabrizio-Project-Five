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
    page = st.sidebar.radio("Choose a page", ["page_1_summary",
                                              "page_2_correlation",
                                              "page_3_prediction",
                                              "page_4_hypothesis",
                                              "page_5_pipeline"])

    if page == "page_1_summary":
        page_1_summary.page_summary_body()
    elif page == "page_2_correlation":
        page_2_correlation.page_correlation_body()
    elif page == "page_3_prediction":
        page_3_prediction.page_prediction_body()
    elif page == "page_4_hypothesis":
        page_4_hypothesis.page_hypothesis_body()
    elif page == "page_5_pipeline":
        page_5_pipeline.page_pipeline_body()

# this logic will allow the app to be ran when calling the "streamlit run 
# app.py" function
if __name__ == "__main__":
    main()
