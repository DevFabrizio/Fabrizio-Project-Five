import streamlit as st
import pandas as pd
import numpy as np
import joblib

# code taken from the Churnometer Project


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_clean_data():
    df = pd.read_csv("outputs/dataset/collection/clean_dataset.csv")
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_fe_data():
    df = pd.read_csv(
        "outputs/dataset/collection/feature_engineered_dataset.csv")
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_houses_data():
    df = pd.read_csv(
        "inputs/datasets/raw/"
        "house-price-20211124T154130Z-001/house-price/inherited_houses.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
