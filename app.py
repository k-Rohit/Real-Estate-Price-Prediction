import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title of the application
st.title("Real Estate Price Predictor")

# Sidebar inputs
st.sidebar.header("Input Features")