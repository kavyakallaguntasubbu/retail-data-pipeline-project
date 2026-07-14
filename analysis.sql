SELECT SUM(Sales) AS total_sales, SUM(Profit) AS total_profit
FROM superstore;

SELECT Product_Name, SUM(Profit) AS profit
FROM superstore
GROUP BY Product_Name
ORDER BY profit DESC
LIMIT 5;

SELECT Discount, AVG(Profit) AS avg_profit
FROM superstore
GROUP BY Discount;

SELECT order_date,
SUM(Sales) OVER (ORDER BY order_date) AS running_sales
FROM superstore;
