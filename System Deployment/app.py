from datetime import datetime
import streamlit as st
import requests
import joblib
from streamlit_lottie import st_lottie
import numpy as np
import pandas as pd

from Process import Calculate_Average_Transaction_Amount,calculate_time_since_last_transaction,encode,Calculate_Time_month,Handle_Category,woe_encoding



st.set_page_config(page_title='Fraud Detection', page_icon='::star::')

def load_lottie(url): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def prepare_input_data_for_model(merchant_name,Category,amount,lname,transaction_date):
    
    woe_encoded_merchant=encode(merchant_name)
    woe_encoded_name=encode(lname)
    category=Handle_Category(Category)
    transaction_month=Calculate_Time_month(transaction_date)
    AverageAmount=Calculate_Average_Transaction_Amount(CardNumber)
    time=calculate_time_since_last_transaction(CardNumber)
      
     
    #Card Number	merchant	category	Amount	lastName	Average Transaction Amount	Time Since Last Transaction		month

    A = [woe_encoded_merchant,category,amount,woe_encoded_name,AverageAmount,time,transaction_month]
    sample1= np.array(A).reshape(-1,len(A))
    return sample1


loaded_model_XG =joblib.load(open("XG_model", 'rb'))
loaded_model_LR =joblib.load(open("LR_model", 'rb'))
loaded_model_KNN =joblib.load(open("KNN_model", 'rb'))
loaded_model_DT =joblib.load(open("DT_model", 'rb'))
loaded_model_RF=joblib.load(open("RF_model", 'rb'))
loaded_model_NB=joblib.load(open("NB_model", 'rb'))

st.write('# Fraud Detection System')
lottie_link= "https://lottie.host/1b2aff3b-6aaf-481a-8f40-dd5b1dbed620/Uli6EJRVc3.json"

st.write('---')

with st.container():
    
    right_column,left_column = st.columns(2)
    
    with right_column:

        st.subheader('"Protect your money, prevent fraud!"')
        
        fname = st.text_input('Card Holder First Name:')
        
        lname = st.text_input('Card Holder Last Name:')
        
        merchant_name_input = st.text_input('Merchant Name:')
        
        CardNumber=st.number_input('Card Number : ')
        
        id= st.number_input('Transaction ID : ')
        
        amount= st.number_input('Transaction Amount : ')
        
        date=st.date_input("Transaction Time: ", datetime(2019, 1, 1))
        
        category=st.selectbox('Category of Merchant : ', ('misc_net', 'grocery_pos', 'entertainment', 'gas_transport',
       'misc_pos', 'grocery_net', 'shopping_net', 'shopping_pos',
       'food dining', 'personal_care', 'health_fitness', 'travel',
       'kids pets', 'home', 'kids'))

        
        sample1= prepare_input_data_for_model(merchant_name_input,category,amount,lname,date)
        #CardNumber,merchant_name,Category,amount,transaction_date
     
     
        if st.button('Fraud Detection Using Decision Tree Model'):
            pred_Y1= loaded_model_DT.predict(sample1)
            if pred_Y1==0:
                st.write("**The Transaction was Legitimate.**")
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
                
        if st.button('Fraud Detection Using  Logistic Regression Model'):
            pred_Y1= loaded_model_LR.predict(sample1)
            if pred_Y1==0:
                st.write('# The Transaction was Legitimate.')
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
                
        if st.button('Fraud Detection Using Random Forest Model'):
            pred_Y1= loaded_model_RF.predict(sample1)
            if pred_Y1==0:
                st.write('# The Transaction was Legitimate.')
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
                
        if st.button('Fraud Detection Using XGBoost Model'):
            pred_Y1= loaded_model_XG.predict(sample1)
            if pred_Y1==0:
                st.write('# The Transaction was Legitimate.')
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
            
        if st.button('Fraud Detection Using Gaussian Naive Bayes Model'):
            pred_Y1= loaded_model_NB.predict(sample1)
            if pred_Y1==0:
                st.write('# The Transaction was Legitimate.')
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
                
        if st.button('Fraud Detection Using KNN Model'):
            pred_Y1= loaded_model_KNN.predict(sample1)
            if pred_Y1==0:
                st.write('# The Transaction was Legitimate.')
            elif pred_Y1==1:
                st.write('# The Transaction was Fraudulent.')
        
    with left_column:
        st_lottie(lottie_link, speed=1, height=400, key="initial")
        
        
        
    
                  