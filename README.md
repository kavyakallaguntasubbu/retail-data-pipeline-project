# retail-data-pipeline-project 
OVERVIEW :
This project demonstrates a mini end-to-end Data Engineering pipeline using MySQL and Python on a retail dataset.
The pipeline includes:
Data ingestion from CSV (Kaggle Superstore dataset)
Data cleaning and transformation using SQL
Business analysis using advanced SQL queries
Data extraction and export using Python

Tech Stack : 
- SQL (MySQL)
- Python (Pandas, MySQL Connector)
- Database: MySQL
- Dataset: Superstore Sales (Kaggle) 

PROJECT STRUCTURE:
retail-data-pipeline-project/
│
├── data/
│   └── superstore.csv
│
├── sql/
│   └── analysis.sql
│
├── python/
│   └── pipeline.py
│
├── README.md 

Pipeline Workflow :
1. Data Ingestion
Imported raw CSV dataset into MySQL table
2. Data Cleaning
Handled missing values
Renamed columns for consistency
Ensured correct data types
3. Data Transformation (SQL)
Aggregated sales and profit
Performed region-wise and product-wise analysis
Analyzed discount impact on profit
Created time-based trends
Used window functions for running totals
4. Data Extraction (Python)
Connected MySQL with Python
Loaded data into Pandas DataFrame
Exported cleaned data to CSV

Key Analysis : 
Total Sales and Profit calculation
Top profitable products
Loss-making products
Discount vs Profit analysis
Region-wise sales performance
Monthly sales trend
Running total using window functions

Sample SQL Queries:
SELECT SUM(Sales) AS total_sales, SUM(Profit) AS total_profit
FROM superstore;

Python Pipeline:
import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="my_project"
)
