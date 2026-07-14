import mysql.connector
import pandas as pd

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "my_project"
}

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**DB_CONFIG)
    print("Connected to database")

    # Query
    query = "SELECT * FROM superstore"

    # Load data
    df = pd.read_sql(query, conn)
    print("Data loaded into DataFrame")

    # Export data
    df.to_csv("cleaned_sales.csv", index=False)
    print("Data exported to CSV successfully")

except Exception as e:
    print("Error:", e)

finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed")
