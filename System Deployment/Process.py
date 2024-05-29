import pandas as pd
import numpy as np
from datetime import datetime
from category_encoders import WOEEncoder  # WOE encoder from category_encoders library

# Load your dataset
df = pd.read_csv("FData.csv")

# Encode categorical variables with WOE (assuming 'merchant' is already WOE-encoded)
# Function to fetch WOE-encoded value of merchant
def encode(merchant_name):
    # Assuming 'df' contains WOE-encoded merchant data
    woe_value = df.loc[df['merchant'] == merchant_name, 'merchant_woe'].values
    if len(woe_value) > 0:
        return woe_value[0]  # Return WOE-encoded value if merchant exists
    else:
        return 0  # Return None if merchant is not found in the WOE-encoded data

def Calculate_Average_Transaction_Amount(card_number):
    # Filter the dataset for transactions with the specified card number
    filtered_data = df[df['Card Number'] == card_number]

    # Calculate the mean of the 'Amount' column for transactions with the specified card number
    mean_amount = filtered_data['Amount'].mean()
    
    return mean_amount
    
def calculate_time_since_last_transaction(card_number):
    # Filter the dataset for transactions with the specified card number
    filtered_data = df[df['Card Number'] == card_number]

    # Check if any transactions are found for the card number
    if len(filtered_data) > 0:
        # Get the time since last transaction for the first transaction (assuming sorted by time)
        time_since_last_transaction = filtered_data.iloc[0]['Time Since Last Transaction']
        return time_since_last_transaction
    else:
        return 0  # Card number not found in the dataset
    
def Calculate_Time_month(transaction_date):
    
    # Extract hour from the transaction date
    transaction_month = transaction_date.month
    return transaction_month


def Handle_Category(Category):
    if Category=='misc_net':
        category=0
        
    elif Category=='grocery_pos':
        category=1
        
    elif Category=='entertainment':
        category=2
        
    elif Category=='gas_transport':
        category=3
        
    elif Category=='misc_pos':
        category=4
        
    elif Category=='grocery_net':
        category=5
        
    elif Category=='shopping_net':
        category=6
        
    elif Category=='shopping_pos':
        category=7
        
    elif Category=='food_dining':
        category=8
        
    elif Category=='personal_care':
        category=9
        
    elif Category=='health_fitness':
        category=10
      
    elif Category=='travel':
        category=11
        
    elif Category=='kids_pets':
        category=12
        
    elif Category=='home':
        category=13
        
    elif Category=='kids_':
        category=14
    return category