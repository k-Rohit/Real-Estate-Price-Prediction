import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle

# Title of the application
st.title("Real Estate Price Predictor")

# Load the DataFrame
with open('pipelines/df_v2.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipelines/pipeline_1.pkl', 'rb') as file:
    pipeline = joblib.load(file)

st.header("Enter your inputs")

# Create two columns
col1, col2 = st.columns(2)

# Column 1 inputs
with col1:
    property_type = st.selectbox('Property Type', ['flat', 'house'])
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
    bedroom = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
    balcony = st.selectbox('Number of Balconies', sorted(df['balcony'].unique().tolist()))
    property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

# Column 2 inputs
with col2:
    built_up_area = float(st.number_input('Enter the desired built up area'))
    
    servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))
    
    store_room = float(st.selectbox('Store Room', [0.0, 1.0]))
    
    furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # Prepare the input data
    data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area,
             servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession', 
               'built_up_area', 'servant room', 'store room', 'furnishing_type', 'luxury_category', 
               'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    # Display the DataFrame (for debugging)
    st.write(one_df)

    try:
        # Make prediction
        prediction = pipeline.predict(one_df)
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = base_price - 0.22
        high = base_price + 0.22

        st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))
    except Exception as e:
        st.error(f"An error occurred: {e}")
