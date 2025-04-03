# %%
import pandas as pd
import sqlite3


# %%
df = pd.read_csv("cleaned_superstore_sales_data.csv")  # Or your file
df['order_date'] = pd.to_datetime(df['order_date'])
# df['Year_Month'] = df['order_date'].dt.to_period('M')
conn = sqlite3.connect("sales_customers.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# %%
df.info()

# %%
df.nunique()

# %% [markdown]
# TOP 10 Customers based on their Total Revenue

# %%
query1 = """
SELECT customer_id, SUM(sales) AS total_revenue
FROM sales
GROUP BY customer_id
ORDER BY SUM(sales) DESC
LIMIT 10;
"""

top_customers = pd.read_sql_query(query1, conn)

# Step 5: Display results
print(top_customers)

# %% [markdown]
# Monthly Revenue Trend

# %%
query2 = """
SELECT strftime('%Y-%m', order_date) AS dt_month, SUM(sales) AS total_revenue
FROM sales
GROUP BY dt_month
ORDER BY dt_month;
"""

monthly_revenue_trend = pd.read_sql_query(query2, conn)

# Step 5: Display results
print(monthly_revenue_trend)

# %% [markdown]
# Total number of Orders made by each Customer and revenue per customer

# %%
que = """
SELECT customer_id, COUNT(DISTINCT order_id) AS num_orders,sum(sales) AS total_rev_cust
FROM sales
GROUP BY customer_id
order by COUNT(DISTINCT order_id)desc

"""

pd.read_sql_query(que, conn)

# %% [markdown]
# Repeated VS One time Customer

# %%
query3 = """
WITH customer_orders AS (
    SELECT customer_id, COUNT(DISTINCT order_id) AS num_orders,sum(sales) AS total_rev_cust
    FROM sales
    GROUP BY customer_id
)

SELECT 
    CASE 
        WHEN num_orders = 1 THEN 'One-Time'
        ELSE 'Repeat'
    END AS customer_type,
    COUNT(*) AS customer_count,
    ROUND(Sum(total_rev_cust),2) AS total_revenue,
    ROUND(AVG(total_rev_cust),2) AS avg_revenue
FROM customer_orders
GROUP BY customer_type;
"""

repeated_one_time_cust = pd.read_sql_query(query3, conn)

# Step 5: Display results
print(repeated_one_time_cust)

# %%
#% of repeat customers
query7="""
WITH customer_orders AS ( 
SELECT customer_id, COUNT(DISTINCT order_id) AS num_orders
    FROM sales
    GROUP BY customer_id
)
SELECT
    ROUND(COUNT(CASE WHEN num_orders > 1 THEN 1 END) * 100.0 / COUNT(*), 2) AS repeat_customer_percentage
FROM customer_orders;
"""

repeat_cust_percentage = pd.read_sql_query(query7, conn)
print(repeat_cust_percentage)

# %% [markdown]
# Identify Customers who have not made Transactions over last 6 months

# %%
que2="""
SELECT MAX(order_date)
FROM sales
"""
pd.read_sql_query(que2, conn)

# %%
query = """
WITH last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date_cust
    FROM sales
    GROUP BY customer_id
),
cutoff AS (
    SELECT DATE(MAX(order_date), '-6 months') AS six_months_ago
    FROM sales
)

SELECT lo.customer_id, lo.last_order_date_cust,c.six_months_ago
FROM last_orders lo, cutoff c
WHERE lo.last_order_date_cust < c.six_months_ago;
"""

inactive_customers = pd.read_sql_query(query, conn)
print(inactive_customers)

# %% [markdown]
# Insight: 
# These customers haven’t transacted in 6+ months — they may be churn risks or need re-engagement offers.
# 
# Some inactive customers are more valuable — so let us find:-
# 
# Inactive customers
# 
# Their total lifetime revenue
# 
# Then filter only those whose revenue > 5000
# 

# %%
query = """
WITH last_orders AS (
    SELECT customer_id, MAX(order_date) AS last_order_date
    FROM sales
    GROUP BY customer_id
),
cutoff AS (
    SELECT DATE(MAX(order_date), '-6 months') AS six_months_ago
    FROM sales
),
inactive_customers AS (
    SELECT lo.customer_id
    FROM last_orders lo, cutoff c
    WHERE lo.last_order_date < c.six_months_ago),

lifetime_spend AS (
    SELECT customer_id, SUM(sales) AS total_revenue
    FROM sales
    GROUP BY customer_id
)

SELECT 
    i.customer_id,
    l.total_revenue
FROM inactive_customers i
JOIN lifetime_spend l ON i.customer_id = l.customer_id
WHERE l.total_revenue > 5000;
"""

high_value_customers = pd.read_sql_query(query, conn)
print(high_value_customers)

# %% [markdown]
# Most Sold Product Categories
# 

# %%
query5="""
SELECT category, SUM(quantity) AS total_sold
FROM sales
GROUP BY category
ORDER BY SUM(quantity) DESC;
 
"""

most_sold_product =pd.read_sql_query(query5, conn)
print(most_sold_product)

# %% [markdown]
# HIGH Revenue Region

# %%
query6="""
SELECT region, round(SUM(sales),2) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;
"""
high_revenue_region = pd.read_sql_query(query6, conn)
print(high_revenue_region)




