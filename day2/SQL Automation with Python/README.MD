# 🧠 SQL Automation – Customer Churn & Sales Insight

This project demonstrates how to automate SQL-based data analysis workflows using Python and SQLite.
It focuses on real-world business problems like customer churn, revenue tracking, and customer behavior.

## 📄 File

### [sql_automation.ipynb](sql_automation.py)
- Uses the `sqlite3` library in Python to query customer transaction data.
- Includes reusable SQL queries automated with Python.
- Core tasks:
  - Identify top 10 customers by revenue
  - Calculate churn-like behavior: customers inactive for 6+ months
  - Segment repeat vs one-time buyers
  - Calculate revenue lost due to inactive customers
  - Filter high-value churned customers (₹5,000+ lifetime spend)

## 📎 Tableau Dashboard Link (View Online)
🔗 [Click here to view the dashboard on Tableau Public](https://public.tableau.com/app/profile/shrishti.agarwal7750/viz/Interactive_Sales_And_Customer_Dashboard/SalesDashboard)
-

## ⚙️ Automation Ready
- All queries are executed from Python using `pandas.read_sql_query()`.
- Final output can be saved as `.csv` or used for scheduled reporting.
- Easily extendable for email automation or dashboard integration.

## 📚 Skills Demonstrated
- SQL + Python integration with SQLite
- Business-focused SQL query design
- Data automation with Python scripts
- Customer behavior and retention analysis

## 💡 Objective
To automate a weekly customer churn report and build logic for identifying high-risk, high-value customers using SQL within Python.

---
