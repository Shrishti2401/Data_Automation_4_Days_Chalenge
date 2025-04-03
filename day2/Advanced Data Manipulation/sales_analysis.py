# %% [markdown]
# 
# # **Performed advanced sales analysis on Superstore dataset using Pandas,**
# # **GroupBy, and Pivot Tables to uncover key business insights.**
# 
# 

# %%
#Using Pivot table and group by in Walmart Sales Data
#Importing Libraries
import pandas as pd


# %%
#Importing Dataset
df = pd.read_csv("Superstore.csv",encoding="ISO-8859-1")
#Checking the first 5 rows of the dataset
print(df.head())
#Checking the shape of the dataset
print(df.shape)
#Checking the columns of the dataset
print(df.columns)
#Checking the data types of the columns
print(df.dtypes)

# %%
df.head(10)

# %%
#Print unique values in each column
print("Unique Values in each Column")
print(df.nunique())


# %%
#Checking the null values in the dataset
print("Total Null Values")
print(df.isnull().sum())

# %%
#Remove any empty spaces in the column names
df.columns = df.columns.str.strip()
#changing column names to lowercase
df.columns = df.columns.str.lower()
#Checking the columns of the dataset after changing the column names
print(df.columns)
#if spaces in between colmn names, remove them replace by "_"
df.columns = df.columns.str.replace(' ', '_')
#remove any character occurence in column name and replace with _
df.columns = df.columns.str.replace('-', '_')

# %%
df_cleaned=df
df_cleaned.to_csv("cleaned_superstore_sales_data.csv", index=False)  # Save cleaned DataFrame to a new CSV file
print("Cleaned DataFrame saved to cleaned_services.csv")

# %%
df.head()

# %% [markdown]
# ## **Problem 1**
# 
# #### Find the Top 3 Most Profitable Product Sub-Categories in Each Region
# #### Goal: Identify which Sub-Categories are generating the highest profit in each region.
# 

# %% [markdown]
# by_group =df.groupby(['region', 'sub_category'],sort=True,as_index=False)['profit'].sum().groupby('region')

# %% [markdown]
# for reg,frame in iter(by_group):
#     print(f"Region: {reg}")
#     print(frame)
#     print("\n")

# %%
profitable_product=df.groupby(['region', 'sub_category'])['profit'].sum().reset_index() \
    .sort_values(['region', 'profit'], ascending=[True, False]) \
    .groupby('region').head(3)

print("Top 3 Sub Categories by Profit in each Region")

for region in profitable_product['region'].unique():
    print(f"\nRegion: {region}")
    region_data = profitable_product[profitable_product['region'] == region]
    for _, row in region_data.iterrows():
        print(f"  Sub-Category: {row['sub_category']}, Profit: {row['profit']}")

# %% [markdown]
# ## **Problem 2**
# ####  Find the Monthly Sales Trend for Each Category
# #### Goal: Show how sales have changed month by month for each product category.

# %%
df['order_date'] = pd.to_datetime(df['order_date'])
df['Year_Month'] = df['order_date'].dt.to_period('M')





# %%


# Verify the column has been removed
print(df.info())

# %%
df.head()

# %%
df.groupby(['Year_Month','category'])['sales'].sum().reset_index().sort_values(['Year_Month','sales'],ascending=[True,False])

# %%
# df[['Year_Month']].dt.year.unique()

#distinct years and length of them in year_month column
print(df['Year_Month'].dt.year.unique())
print(len(df['Year_Month'].dt.year.unique()))

# %%

# Get the distinct years
distinct_years = df['Year_Month'].dt.year.unique().tolist()
print("Distinct Years:", distinct_years)
print("Length of Distinct Years:", len(distinct_years))
distinct_years.sort()
print("Sorted Distinct Years:", distinct_years)

# %%
for y in range(len(distinct_years)):
    year = distinct_years[y]
    print(f"Year: {year}")
    df_y = df[df['Year_Month'].dt.year == year]
    monthly_sales = df_y.pivot_table(index='Year_Month', columns='category', values='sales', aggfunc='sum').reset_index()
    print(monthly_sales)

# %% [markdown]
# ## **Problem 3**
# #### Identify Customers with the Most Repeat Purchases
# #### Goal:Find customers who have placed the most orders (not based on sales, but count of transactions).

# %%
#the number of distinct orders placed by a customer, regardless of how many products were in each order.
df.groupby('customer_name')['order_id'].nunique().sort_values(ascending=False).head(10)

# %%
# counts every single product customer ordered
df.groupby('customer_name')['order_id'].count().nlargest(15)

# %% [markdown]
# ## **Problem 4**
# #### Find the Average Discount Given in Each State
# #### Goal: Understand which states receive higher discounts on average.
# 
# 

# %%
df.head()

# %%
#convert discount column in floating type to percentage
df['discount'] = df['discount'].astype(float) * 100
df.head()

# %%
df.info()
#convert discount column in percentage to float type
df['discount'] = df['discount'].astype(float) / 100
df.head()

# %%
#pd.set_option("display.float_format", "{:.2%}".format)
#reset options to default
pd.reset_option("display.float_format")

df.groupby('state')['discount'].mean().sort_values(ascending=False)

# %% [markdown]
# ### **Problem 5**
# ##### Determine the Most Popular Ship Mode in Each Region
# 
# ###### Goal:Find out which shipping mode (Standard Class, Second Class, etc.) is the most used in each region.

# %%
list_ship_mode=df['ship_mode'].unique().tolist()

# %%
#SOLUTION 1
#Using Cross tab to count unique values in ship_mode column for each region
pd.crosstab(df["region"], df["ship_mode"])

# %%
#SOLUTION 2
df.groupby(['region', 'ship_mode'])['order_id'].count().reset_index() \
    .sort_values(['region', 'order_id'], ascending=[True, False]) \
    .groupby('region').first()

# %% [markdown]
# ## Skills Gain:
# #### group_by()
# #### sorting,
# #### pivot_table(),
# #### cross_tab(),
# #### dt.to_period(),
# #### nunique()


