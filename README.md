# 🔮 Retail Demand Forecasting Project

## 📝 Objective

The goal of this project is to build a predictive model that accurately forecasts **product demand** across multiple stores and regions. Effective demand forecasting enables better inventory planning, minimizes stockouts or overstocking, and enhances profitability in the retail supply chain.

---

## 📁 Dataset Overview

This dataset consists of **73,100 records** capturing historical sales, product, store, and environmental data.

### 📊 Features Summary

| Column Name           | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `Date`                | Date of the record (daily granularity)                                      |
| `Store ID`            | Unique identifier for each store                                            |
| `Product ID`          | Unique identifier for each product                                          |
| `Category`            | Product category (e.g., Electronics, Clothing)                              |
| `Region`              | Geographic region                                                           |
| `Inventory Level`     | Inventory available on that day                                             |
| `Units Sold`          | Actual units sold                                                           |
| `Units Ordered`       | Units requested from suppliers                                              |
| `Demand Forecast`     | (May be ignored or used as a baseline)                                      |
| `Price`               | Retail price of the product                                                 |
| `Discount`            | Discount applied (%)                                                        |
| `Weather Condition`   | Weather during that day (Sunny, Rainy, etc.)                                |
| `Holiday/Promotion`   | 1 if there was a holiday or promotional campaign                            |
| `Competitor Pricing`  | Price of the same/similar product from competitors                          |
| `Seasonality`         | Season or marketing cycle (e.g., Winter, Holiday Season, Back-to-School)    |

---

## 🎯 Target Variable

**`Units Sold`** will be predicted as the proxy for **demand**, based on store, product, pricing, and contextual factors.

---

## 🛠️ Project Workflow

### 🔹 1. Data Preprocessing
- Convert `Date` to datetime format
- Extract month, day, weekday, etc.
- Handle missing values (e.g., price, competitor pricing)
- Encode categorical variables (`Category`, `Region`, `Weather Condition`, `Seasonality`)

### 🔹 2. Feature Engineering
- `Price Gap = Price - Competitor Price`
- `Discounted Price = Price * (1 - Discount/100)`
- Rolling mean of `Units Sold` (e.g., last 7 or 30 days)
- Lag features (e.g., sales yesterday, last week, etc.)
- Holiday/weekend flag from `Date`

### 🔹 3. Visualization
- Actual vs Predicted demand plots
- Feature importance (especially price, discount, region)
- Seasonality and trend charts
- Heatmaps by month/region/store
  
### 🔹 4. Train-Test Split
- Use time-based splitting (e.g., last 3 months as test set)

### 🔹 4. Modeling
- Try the following regressors:
  - `LinearRegression`
  - `ElasticNet`
  - `Lasso & Ridge`
  - `RandomForestRegressor`
  - `XGBRegressor`
  - `GradientBoostingRegressor`

### 🔹 5. Evaluation Metrics
Use regression metrics to evaluate forecast performance:
- `MAE` – Mean Absolute Error
- `RMSE` – Root Mean Squared Error
- `R² Score` – Coefficient of Determination


---

## 🧠 Business Use-Cases

- Improve stock replenishment cycles
- Optimize promotional pricing and discounts
- Plan for holidays and high-demand seasons
- Analyze regional demand differences

---

> 🚀 *Goal:* A well-generalized, explainable model that consistently predicts demand across products, stores, and seasonal cycles.
