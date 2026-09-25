import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def generate_sales_forecast():
    # Load historical sales dataset
    sales_df = pd.read_csv('historical_sales.csv')
    
    # Feature Engineering for time-series modeling
    sales_df['date'] = pd.to_datetime(sales_df['transaction_date'])
    sales_df['month_num'] = sales_df['date'].dt.month
    
    X = sales_df[['month_num', 'historical_units_sold', 'marketing_spend']]
    y = sales_df['revenue']
    
    # Train Forecasting Model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict Future Revenue
    sales_df['forecasted_revenue'] = model.predict(X)
    
    print("--- SALES FORECASTING ENGINE ---")
    print(f"Total Forecasted Revenue: ${sales_df['forecasted_revenue'].sum():,.2f}")
    print("Model Training Successful!")

if __name__ == "__main__":
    generate_sales_forecast()
