from sched import scheduler


import pandas as pd
import openpyxl
import requests
from bs4 import BeautifulSoup  # Correct way to import BeautifulSoup from beautifulsoup4
import smtplib
from sched import scheduler

import pandas as pd  

# Load Excel file  
df = pd.read_csv("services.csv")
# print(df.isnull().sum()) # Check for missing values in the DataFrame
print(df.head)  

# df = df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace from column names
total_rows = len(df)


print("Total Rows:", total_rows)

print("Drop duplicates:", df.duplicated().sum())  # Check for duplicate rows
if df.duplicated().sum():
    df=df.drop_duplicates()  # Drop duplicate rows
print("Total Rows after dropping duplicates:", len(df))




# Check for missing values in the DataFrame
print("Missing values in each column:")
print(df.isnull().sum())
#collect column names having null values
missing_columns = df.columns[df.isnull().any()].tolist()
print("Columns with missing values:", missing_columns)
#if column have more that 90% null values then drop that column
for col in missing_columns:
    if df[col].isnull().mean() > 0.9:
        df.drop(col, axis=1, inplace=True)
        print(f"Dropped column: {col}")



# print remaining columns after dropping columns with more than 90% null values
print("Remaining columns after dropping columns with more than 90% null values:")
col_name=df.columns.tolist()
print(col_name)


# Drop rows where 'Service Name', 'Service ID', or 'Service URL' is NaN


# df.dropna(subset=['Service Name'], inplace=True)  # Drop rows where 'Service Name' is NaN
# df.dropna(subset=['Service ID'], inplace=True)  # Drop rows where 'Service ID' is NaN
# df.dropna(subset=['Service URL'], inplace=True)  # Drop rows where 'Service URL' is NaN


# Check for missing values in the DataFrame after dropping rows
print("Missing values in each column after dropping rows:")
print(df.isnull().sum())

#check all the values in each column
print("All values in each column:")
# Print unique values for all the column
for col in df.columns:
    print(f"Unique values in {col}:")
    print(df[col].unique())

df= df.fillna('')  # Fill NaN values with empty strings

# dropping index values for some particular condition
#reset index after dropping rows
# df = df.reset_index(drop=True)
# print("DataFrame after resetting index:")

df_cleaned=df
df_cleaned.to_csv("cleaned_services.csv", index=False)  # Save cleaned DataFrame to a new CSV file
print("Cleaned DataFrame saved to cleaned_services.csv")