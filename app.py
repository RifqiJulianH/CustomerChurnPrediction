import streamlit as st
import pandas as pd
import joblib
import numpy as np
import tensorflow
import keras

def app():
    
    st.title('[Page 1')
    st.subheader('MILESTONE 1 Phase 2')
    st.write('Author : Rifqi Julian Hasyari')
    st.write('Batch : HCK 006')
    @st.cache_data
    def fetch_data():
        Data = pd.read_csv('churn.csv')
        return Data

    Data = fetch_data()
    age = st.number_input('age',value=1.0)
    gender = st.selectbox('gender',Data['gender'].unique())
    region_category = st.selectbox('region_category',Data['region_category'].unique())
    membership_category = st.selectbox('membership_category',Data['membership_category'].unique())
    joining_date = st.number_input('joining_date',value=1.0)
    joined_through_referral = st.selectbox('joined_through_referral',Data['joined_through_referral'].unique())
    preferred_offer_types = st.selectbox('preferred_offer_types',Data['preferred_offer_types'].unique())
    medium_of_operation = st.selectbox('medium_of_operation',Data['medium_of_operation'].unique())
    internet_option = st.selectbox('internet_option',Data['internet_option'].unique())
    last_visit_time = st.slider('last_visit_time', min_value=1, max_value=24, value=2, step=1)
    days_since_last_login = st.slider('days_since_last_login', min_value=0, max_value=30, value=2, step=1)
    avg_time_spent = st.number_input('avg_time_spent',value=1.0)
    avg_transaction_value = st.number_input('avg_transaction_value',value=1.0)
    avg_frequency_login_days = st.number_input('avg_frequency_login_days',value=1.0)
    points_in_wallet = st.number_input('points_in_wallet',value=1.0)
    used_special_discount = st.selectbox('used_special_discount',Data['used_special_discount'].unique())
    offer_application_preference = st.selectbox('offer_application_preference',Data['offer_application_preference'].unique())
    past_complaint = st.selectbox('past_complaint',Data['past_complaint'].unique())
    complaint_status = st.selectbox('complaint_status',Data['complaint_status'].unique())
    feedback = st.selectbox('feedback',Data['feedback'].unique())


    data = {
        'age':age, 
        'gender':gender, 
        'region_category':region_category, 
        'membership_category': membership_category,
        'joining_date':joining_date,
        'joined_through_referral':joined_through_referral,
        'preferred_offer_types':preferred_offer_types,
        'medium_of_operation':medium_of_operation, 
        'internet_option':internet_option, 
        'last_visit_time':last_visit_time,
        'days_since_last_login':days_since_last_login,
        'avg_time_spent':avg_time_spent,
        'avg_transaction_value':avg_transaction_value, 
        'avg_frequency_login_days':avg_frequency_login_days,
        'points_in_wallet':points_in_wallet,
        'used_special_discount':used_special_discount, 
        'offer_application_preference':offer_application_preference,
        'past_complaint':past_complaint,
        'complaint_status':complaint_status,
        'feedback':feedback,
    }
    input = pd.DataFrame(data, index=[0])


    st.subheader('User Input')
    st.write(input)

    load_model = joblib.load("ModelMilestone.pkl")

    if st.button('Predict'):
        prediction = load_model.predict(input)

        if prediction == '0':
            prediction = 'not churn'
        elif prediction == '1':
            prediction = 'churn'

        st.write('Berdasarkan input, pelanggan akan : ')
        st.write(prediction)

if __name__ == '__main__':
    app()

