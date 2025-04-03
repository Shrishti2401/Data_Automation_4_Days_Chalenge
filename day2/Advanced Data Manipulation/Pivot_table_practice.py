# %%
# %pip install pandas
# %pip install matplotlib
import pandas as pd


# %%
df=pd.read_excel("Sales.xlsx", sheet_name="Raw Data")


# %%
df.tail()

# %%
df.to_csv("Sales.csv", index=False)

# %%
import pyarrow

# %%
sales_data =pd.read_csv("Sales.csv",
                          parse_dates=["OrderDate"],
                          dayfirst=True,).convert_dtypes(dtype_backend="pyarrow")


# %%
filtered_data = sales_data[(sales_data['customertype'] == 'Business') & (sales_data['ordertype'] == 'Retail')]

# Display the filtered data
print(filtered_data)

# %%
sales_data.info()

# %%
#Trim spaces in column names
sales_data.columns = sales_data.columns.str.strip() 

# %%
#Trim spaces in column names all whitespace
sales_data.columns = sales_data.columns.str.replace(r"\s+", "_", regex=True)
#Convert to lowercase   
sales_data.columns = sales_data.columns.str.lower()



# %%
sales_data.info()

# %%
df_cleaned=sales_data
df_cleaned.to_csv("cleaned_sales_data.csv", index=False)  # Save cleaned DataFrame to a new CSV file
print("Cleaned DataFrame saved to cleaned_services.csv")

# %%
df_cleaned.info()

# %%
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data.pivot_table(
          values="price", index="sales_region", columns="ordertype",
          aggfunc="sum",)

# %%
#Including totals in the pivot table
sales_data.pivot_table(
          values="price", index="sales_region", columns="ordertype",
          aggfunc="sum", margins=True, margins_name="Total",)

# %%
#Using sub-columns in pivot tables
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data.pivot_table(
          values="price", index="sales_region", columns=["customertype","ordertype"],
          aggfunc="mean",)


# %%
sales_data.head()

# %%
#Create a pivot table that shows the highest sale price for each sales region by product category. 
# This time, each sales region should be in a separate column, and each product category in a separate row.



#Using sub-columns in pivot tables
pd.set_option("display.float_format", "${:_.2f}".format)

sales_data.pivot_table(values="price", index="prodcategory",columns="sales_region",aggfunc="max", )

# %%
#Create a pivot table that shows the highest quantities of each product category within each type of customer. 
# Your pivot table should contain a row for each state the customers live in.
#  Add in summary totals with a "Max Quantity" label.

#Using sub-columns in pivot tables
pd.set_option("display.float_format", "${:_.2f}".format)

sales_data.pivot_table(values="price", index="custstate",columns=["customertype","prodcategory"],aggfunc="max",
                       margins=True, margins_name="Max Quantity",fill_value=0,)





# %%
#This time, you want a pivot table that shows the total product quantities sold analyzed by customer state 
# within order type, and by product category within customer type. You should replace the <NA> values with zeros.

#USING SUBROWS AND SUBCOLUMNS IN PIVOT TABLES
# pd.set_option("display.float_format", "${:,.2f}".format)

sales_data.pivot_table(values="quantity", index=["ordertype","custstate"],columns=["customertype","prodcategory"],aggfunc="sum",
                       fill_value=0, )


# %%
#Using Multiple Values in Pivot Tables
pd.set_option("display.float_format", "${:,.2f}".format)

sales_data.pivot_table(
    index=["sales_region", "prodcategory"],
    values=["quantity","price"],
    aggfunc="sum", fill_value=0,
)

# %%
#Uing .loc[] attribute to allow define the rows and columns by their index labels.


pd.set_option("display.float_format", "${:,.2f}".format)

sales_data.pivot_table(
    index=["sales_region", "prodcategory"],
    values=["quantity","price"],
    aggfunc="sum", fill_value=0,
).loc[:, ["quantity","price"]]




# %%
#Suppose you want to find out more about your company’s sales. 
# Create a pivot table with rows that analyze the different order types by each type of customer,
#  and with columns that show the total quantity for each category of product, 
# as well as the total sales for each category of product ordered.

# %%

# Create a pivot table
sales_data.pivot_table(
    values=["quantity", "order_total"],  # Columns to aggregate
    index=["customertype", "ordertype"],  # Rows: Customer type and order type
    columns=["prodcategory"],  # Columns: Product category
    aggfunc="sum",  # Aggregation function: Sum
    fill_value=0  # Replace NaN with 0
)

#

# %%
#Calculate the maximum and minimum sales of each category of product for each type of customer.

sales_data.pivot_table(index="prodcategory",columns="customertype",values="order_total",
                       aggfunc=["max","min"],fill_value=0,)

# %%
#Adjust the previous analysis to display both the average sale price and the maximum quantity sold.

sales_data.pivot_table(index="prodcategory",columns="customertype",values=["order_total","quantity"],
                       aggfunc={"order_total": "mean", "quantity": "max"})

# %%
sales_data.info()

# %%
# Calculate how many employees there are in each sales region.
sales_data.pivot_table(
    values="empid",
    index="sales_region",
    aggfunc="count",
)


# %%
#Above code is giving wrong answer

def count_unique(values):
    return len(values.unique())

# Corrected code to count unique employee IDs
sales_data.pivot_table(
	values="empid",
	index=["sales_region"],
	aggfunc=count_unique,
)

# %%
sales_data.head(20)

# %%
#determine how many unique products the organization sells in each sales region, 
# and the total income made in each region.

sales_data.pivot_table(values=["prodname","order_total"], index="sales_region",
                       aggfunc={"prodname":count_unique,"order_total":"sum"},fill_value=0,)



# %%
# Using agg function to pass one or more tuples containing the data column and aggregation function 

sales_data.groupby("prodcategory").agg(
	low_price=("price", "min"),
	average_price=("price", "mean"),
	high_price=("price", "max"),
	standard_deviation=("price", "std"),
)

# %%
sales_data.info()

# %%
#Using crosstab

pd.set_option("display.float_format", "{:.2%}".format)

pd.crosstab(
	index=sales_data["employee_job_title"],
	columns=sales_data["sales_region"],
	margins=True,
	margins_name="Totals",
	normalize=True,
)

# %%



