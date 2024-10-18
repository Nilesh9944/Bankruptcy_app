import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)




import streamlit as st

import numpy as np

# Load the model
model = 'xgboost_model.pkl'

# Define the user interface
st.title("Bankruptcy Prediction")
st.write("Enter the details below to predict the bankruptcy")

# Collect user input
Net_Income_to_Stockholder_Equity = st.number_input('Net Income to Stockholders Equity :', min_value=0.0, max_value=1.0, value=0.84)
Borrowing_dependency = st.number_input('Borrowing Dependency', min_value=0.0, max_value=100.0, value=0.37)
Persistent_EPS_in_the_Last_Four_Seasons = st.number_input('Persistent EPS in the Last Four Seasons:', min_value=0.0, max_value=1.0, value=0.22)
Net_profit_before_tax_Paid_in_capital = st.number_input(' Net profit before tax/Paid-in capital:', min_value=0.0, max_value=1.0, value=0.18)
Liability_to_Equity = st.number_input('Liability to Equity:', min_value=0.0, max_value=1.0, value=0.28)
Degree_of_Financial_Leverage = st.number_input('Degree of Financial Leverage (DFL):', min_value=0.0, max_value=1.0, value=0.02)
Net_Value_Per_Share = st.number_input('Net Value Per Share (A):', min_value=0.0, max_value=1.0, value=0.19)
Per_Share_Net_profit_before_tax = st.number_input('Per Share Net profit before tax (Yuan ¥):', min_value=0.0, max_value=1.0, value=0.18)
Net_worth_Assets = st.number_input('Net worth/Assets:', min_value=0.0, max_value=1.0, value=0.89)
Interest_Expense_Ratio = st.number_input('Interest Expense Ratio:', min_value=0.0, max_value=1.0, value=0.63)
Net_Value_Per_Share_B = st.number_input('Net Value Per Share (B):', min_value=0.0, max_value=1.0, value=0.19)
Non_industry_income_and_revenue = st.number_input('Non-industry income and expenditure/revenue:', min_value=0.0, max_value=1.0, value=0.3)
Debt_ratio = st.number_input('Debt ratio %:', min_value=0.0, max_value=1.0, value=0.11)
ROAC_before_interest_and_depreciation_before_interest = st.number_input('ROA(C) before interest and depreciation before interest:', min_value=0.0, max_value=1.0, value=0.50)
Interest_Coverage_Ratio = st.number_input('Interest Coverage Ratio (Interest expense to EBIT):', min_value=0.0, max_value=1.0, value=0.56)
# Make prediction when the user clicks the button
if st.button('Predict'):
    # Prepare the feature vector
    input_data = np.array([[' Net Income to Stockholder\'s Equity', ' Borrowing dependency',
                ' Persistent EPS in the Last Four Seasons', ' Net profit before tax/Paid-in capital',
                ' Liability to Equity', ' Degree of Financial Leverage (DFL)',
                ' Net Value Per Share (A)', ' Per Share Net profit before tax (Yuan ¥)',
                ' Net worth/Assets', ' Interest Expense Ratio', ' Net Value Per Share (B)',
                ' Non-industry income and expenditure/revenue', ' Debt ratio %',
                ' ROA(C) before interest and depreciation before interest',
                ' Interest Coverage Ratio (Interest expense to EBIT)']])
    
    # Predict using the model
    prediction = model.predict(input_data)[0]
    
    # Display the prediction
    st.write(f"Predicted Bankruptcy: {prediction} ")