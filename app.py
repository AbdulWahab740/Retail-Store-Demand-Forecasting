import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("Retail Forecast lasso.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🛍️ Retail Demand Forecasting")
st.write("Enter product and market details to predict demand.")

# ========== USER INPUT ==========

# Numerical Inputs
inventory = st.slider("Inventory", 50, 500, 270)
sales = st.slider("Sales", 0, 434, 100)
orders = st.slider("Orders", 20, 200, 100)
price = st.slider("Price", 10.0, 100.0, 55.0)
discount = st.slider("Discount", 0.0, 20.0, 10.0)
promotion = st.selectbox("Promotion Active", [0, 1])
competitor_price = st.slider("Competitor Price", 5.0, 105.0, 55.0)
month = st.selectbox("Month", list(range(1, 13)))
days = st.selectbox("Day of Month", list(range(1, 32)))

# Category
category = st.selectbox("Category", ['Groceries', 'Toys', 'Electronics', 'Furniture', 'Clothing'])
category_electronics = 1 if category == "Electronics" else 0
category_furniture = 1 if category == "Furniture" else 0
category_groceries = 1 if category == "Groceries" else 0
category_toys = 1 if category == "Toys" else 0
# Clothing = baseline (0 for all)

# Region
region = st.selectbox("Region", ['North', 'South', 'West', 'East'])
region_north = 1 if region == "North" else 0
region_south = 1 if region == "South" else 0
region_west = 1 if region == "West" else 0
# East = baseline

# Weather
weather = st.selectbox("Weather", ['Rainy', 'Sunny', 'Cloudy', 'Snowy'])
weather_rainy = 1 if weather == "Rainy" else 0
weather_snowy = 1 if weather == "Snowy" else 0
weather_sunny = 1 if weather == "Sunny" else 0
# Cloudy = baseline

# Seasonality
season = st.selectbox("Season", ['Autumn', 'Summer', 'Winter', 'Spring'])
season_spring = 1 if season == "Spring" else 0
season_summer = 1 if season == "Summer" else 0
season_winter = 1 if season == "Winter" else 0
# Autumn = baseline

# ========== PREDICTION ==========
if st.button("Predict Demand"):
    input_features = np.array([[
        inventory, sales, orders, price, discount, promotion, competitor_price,
        month, days,
        category_electronics, category_furniture, category_groceries, category_toys,
        region_north, region_south, region_west,
        weather_rainy, weather_snowy, weather_sunny,
        season_spring, season_summer, season_winter
    ]])

    demand_prediction = model.predict(input_features)[0]
    st.success(f"📦 Predicted Demand: **{demand_prediction:.2f} units**")
