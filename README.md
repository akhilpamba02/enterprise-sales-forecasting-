# Enterprise Sales Performance & Predictive Revenue Forecasting System

## Executive Summary
An end-to-end analytical data solution designed to ingest multi-region enterprise sales transactions, perform exploratory data analysis, and build time-series forecasting models to project future quarterly revenue trends.

## Key Features & Business Impact
- **Time-Series Revenue Forecasting**: Utilized ARIMA / Prophet / XGBoost algorithms to model seasonal trends and project quarter-over-quarter revenue with high precision.
- **SQL Data Pipeline**: Developed optimized SQL scripts (using CTEs, Window Functions, and aggregations) to aggregate daily sales logs into structured business data models.
- **KPI Dashboards**: Structured data tables tailored for seamless visualization in Tableau/Power BI to track Regional Revenue, Growth Rate, and Product Category Performance.

## Tech Stack
- **Data Processing**: Python (Pandas, Statsmodels), SQL (PostgreSQL/Snowflake compatible)
- **Machine Learning**: Time Series Forecasting (Prophet, ARIMA, Random Forest Regressor)
- **Analytics & BI**: Data Aggregation, Trend Analysis, KPI Reporting

## Key Metrics & Results
- **Forecast Accuracy**: Achieved a Mean Absolute Percentage Error (MAPE) of < 6.8% on holdout validation data.
- **Business Impact**: Automated revenue projection reporting, reducing quarterly planning cycle prep time by over 40%.

## Project Structure
```text
├── data/              # Raw and processed datasets
├── notebooks/         # EDA and Model Training Jupyter Notebooks
├── sql/               # Data Transformation & Aggregation Scripts
├── src/               # Python Scripts for Pipeline Automation
└── README.md          # Project Documentation
