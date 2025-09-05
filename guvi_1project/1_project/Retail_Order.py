import streamlit as st     # import streamlit

a=st.sidebar.selectbox('select any one',['1 Find top 10 highest revenue generating products',
                     '2 Find the top 5 cities with the highest profit margins',
                     '3 Calculate the total discount given for each category',
                     '4 Find the average sale price per product category',
                     '5 Find the region with the highest average sale price',
                     '6 Find the total profit per category',
                     '7 Identify the top 3 segments with the highest quantity of orders',
                     '8 Determine the average discount percentage given per region',
                     '9 Find the product category with the highest total profit',
                     '10 Calculate the total revenue generated per year',
                     '11 Find total sales per category.',
                     '12 Find average discount per sub-category.',
                     '13 Get top 5 customers by total spending.',
                     '14 Find total number of orders placed in each region.',
                     '15 Calculate total sales with and without discount for each category.',
                     '16 Find products that had more than 20% average discount.',
                     '17 Show monthly sales trend.',
                     '18 Find the sub-category that generated the highest sales in each region.',
                     '19 Find customers who placed more than 5 orders.',
                     '20 Calculate revenue  per sub-category.']
                     )

#!pip install pandas sqlalchemy pymysql
from sqlalchemy import create_engine
import pandas as pd
import pymysql

dic={'1 Find top 10 highest revenue generating products': """select Sub_Category, sale_price from retail_order_2 order by sale_price desc limit 10;""",
     '2 Find the top 5 cities with the highest profit margins':"""select a.City , b.profit from retail_order_1 as a inner join  retail_order_2 as b on a.order_id=b.order_id order by b.profit desc limit 5;""",
     '3 Calculate the total discount given for each category':"""select a.Category , count(discount) from retail_order_1 as a inner join  retail_order_2 as b on a.order_id=b.order_id  group by a.Category ;""",
     '4 Find the average sale price per product category':"""select Sub_Category , avg(discount) from retail_order_1 as a inner join  retail_order_2 as b on a.order_id=b.order_id  group by Sub_Category ;""",
     '5 Find the region with the highest average sale price':"""select a.Region,avg(b.sale_price) as highest_average from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id group by a.Region ;""",
     '6 Find the total profit per category':"""select a.Category ,count(b.profit) as total_profit_per_category   from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id group by a.Category;""",
     '7 Identify the top 3 segments with the highest quantity of orders':"""select a.Segment  from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id order by  b.Quantity desc limit 3;""",
     '8 Determine the average discount percentage given per region':"""select a.Region, avg(b.Discount_Percent) as average_discount_percentage from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id group by a.Region ;""",
     '9 Find the product category with the highest total profit':"""select a.Category, count(b.profit) as highest_total_profit from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id group by a.Category order by highest_total_profit  desc;""",
     '10 Calculate the total revenue generated per year':"""select  year(a.Order_Date) as year , count(b.profit) as total_revenue_generated_per_year  from retail_order_1 as a inner join retail_order_2 as b on a.order_id=b.order_id   group by year  ;""",
     '11 Find total sales per category.':"""select Category ,sum(sale_price) as total_sales  from retail_order_1 as a  inner join  retail_order_2 as b on a.order_id=b.order_id  group by Category order by total_sales  DESC;""" ,
     '12 Find average discount per sub-category.':"""select Sub_Category , avg(discount) as average_discount from retail_order_1 as a  inner join  retail_order_2 as b on a.order_id=b.order_id group by  Sub_Category ;""",
     '13 Get top 5 customers by total spending.':"""SELECT Product_Id, SUM(b.sale_price ) AS total_spent FROM retail_order_1 as  a JOIN retail_order_2 as  b ON a.order_id = b.order_idGROUP BY Product_Id ORDER BY total_spent DESC LIMIT 5;""",
     '14 Find total number of orders placed in each region.':"""SELECT a.Region, COUNT( a.order_id) AS order_count FROM retail_order_1 a GROUP BY a.Region ORDER BY order_count DESC;""",
     '15 Calculate total sales with and without discount for each category.':"""SELECT a.Category,SUM(b.sale_price) AS total_sales FROM retail_order_1 a JOIN retail_order_2 b ON a.order_id = b.order_id GROUP BY a.Category;""",
     '16 Find products that had more than 20% average discount.':"""SELECT b.product_id, AVG(b.discount) AS avg_discount FROM retail_order_2 b GROUP BY b.product_id HAVING avg_discount > 20;""",
     '17 Show monthly sales trend.':"""SELECT month(a.order_date) AS month,year(a.order_date) as year ,SUM(b.sale_price) AS total_sales FROM retail_order_1 a JOIN retail_order_2 b ON a.order_id = b.order_id GROUP BY month(a.order_date) ,year order by year ,month ;""",
     '18 Find the sub-category that generated the highest sales in each region.':"""SELECT a.Region, b.Sub_Category, SUM(b.sale_price) AS total_sales FROM retail_order_1 a  inner join retail_order_2 b ON a.order_id = b.order_id GROUP BY a.Region, b.Sub_Category ORDER BY a.Region ,total_sales DESC;""",
     '19 Find customers who placed more than 5 orders.':"""SELECT City, COUNT( a.order_id) AS order_count FROM retail_order_1 a GROUP BY City HAVING order_count > 5;""",
     '20 Calculate revenue  per sub-category.':"""SELECT Sub_Category,SUM(b.sale_price) AS total_sales FROM retail_order_1 a JOIN retail_order_2 b ON a.order_id = b.order_id GROUP BY Sub_Category ORDER BY total_sales DESC;"""}

import  pymysql
user = 'root'
password = '#San4533t'
host = '127.0.0.1'  
my_connection=pymysql.connect(host = '127.0.0.1' ,user = 'root',password = '#San4533t',port = 3306 ,database = 'guvi_project1')
df=pd.read_sql_query(dic[a],my_connection )
st.write(df)