# retail-data-pipeline-project 
OVERVIEW :
Built an end-to-end retail data pipeline using Python, Pandas, and MySQL, enabling analytical insights on sales performance across regions and customers.
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
├── superstore.csv       # Raw dataset
├── analysis.sql         # SQL transformation & analysis queries
├── pipeline.py          # Python script for ingestion/extraction
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
import os
from dotenv import load_dotenv
load_dotenv()
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}
conn = mysql.connector.connect(**DB_CONFIG)
