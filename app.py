import streamlit as st

from app_pages import (
    page_1_summary,
    page_2_correlation,
    page_3_prediction,
    page_4_hypothesis,
    page_5_pipeline
)


def main():
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


if __name__ == "__main__":
    main()
