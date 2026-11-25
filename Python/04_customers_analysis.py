import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Customers Dataset
customers_df = pd.read_csv(
    "Data/Raw/olist_customers_dataset.csv"
)

# Display first 5 records
print("First 5 Records:")
print(customers_df.head())

# Dataset Shape
print("\nDataset Shape:")
print(customers_df.shape)

# Dataset Columns
print("\nDataset Columns:")
print(customers_df.columns)

# Dataset Information
print("\nDataset Information:")
print(customers_df.info())
#checking missing values
print("Missing Values:")
print(customers_df.isnull().sum())
#checking duplicate records
print("Full Duplicate Rows:")
print(customers_df.duplicated().sum())

print("\nDuplicate Customer IDs:")
print(customers_df["customer_id"].duplicated().sum())

print("\nDuplicate Unique Customer IDs:")
print(customers_df["customer_unique_id"].duplicated().sum())
#Total customer records
print("Total Customer Records:")
print(len(customers_df))
#	Total different customers
print("\nTotal Unique Customers:")
print(customers_df["customer_unique_id"].nunique())
#Number of repeated records after first occurrences
print("\nCustomers with Multiple Records:")
print(customers_df["customer_unique_id"].duplicated().sum())
#Calculate how many times the customer made a order
customer_order_counts = customers_df["customer_unique_id"].value_counts()

print("Customer Record Count Distribution:")
print(customer_order_counts.value_counts().sort_index())
#Calculate the repeat customer percentage
repeat_customers = (customer_order_counts > 1).sum()

total_unique_customers = customers_df["customer_unique_id"].nunique()

repeat_customer_percentage = (
    repeat_customers / total_unique_customers
) * 100

print("Repeat Customers:", repeat_customers)
print("Repeat Customer Percentage:", round(repeat_customer_percentage, 2), "%")
#checking blank values in city and state column
print("Blank Customer Cities:")
print((customers_df["customer_city"].str.strip() == "").sum())

print("\nBlank Customer States:")
print((customers_df["customer_state"].str.strip() == "").sum())
#check which Brazilian states have the highest number of customer records
print("Customer Records by State:")
print(customers_df["customer_state"].value_counts())
#calculating statewise percenatge
state_percentage = (
    customers_df["customer_state"].value_counts(normalize=True) * 100
)

print("Customer Percentage by State:")
print(state_percentage.round(2))
#analyszing customer distiburtion by city
print("Top 10 Customer Cities:")
print(customers_df["customer_city"].value_counts().head(10))
#loading order  dataset
orders_df = pd.read_csv(
    "Data/cleaned/orders_cleaned.csv"
)

print("Orders Dataset Shape:")
print(orders_df.shape)
#mergining the customer dataset with the order dataset
customers_orders = customers_df.merge(
    orders_df,
    on="customer_id",
    how="left",
    indicator=True
)

print("Merge Results:")
print(customers_orders["_merge"].value_counts())
#checking ooriginal and merged datset shape
print("Customers Dataset Shape:")
print(customers_df.shape)

print("\nMerged Dataset Shape:")
print(customers_orders.shape)
#finding minimum and maximum value from the postal code column
print("Postal Code Prefix - Minimum:")
print(customers_df["customer_zip_code_prefix"].min())

print("\nPostal Code Prefix - Maximum:")
print(customers_df["customer_zip_code_prefix"].max())
#copying tthe customer data and chaning the datatype of the postall code column from int to str
customers_cleaned = customers_df.copy()

customers_cleaned["customer_zip_code_prefix"] = (
    customers_cleaned["customer_zip_code_prefix"]
    .astype(str)
    .str.zfill(5)
)
#verifying the datatype of the postalcode
print(customers_cleaned[
    "customer_zip_code_prefix"
].head(10))

print("\nPostal Code Data Type:")
print(customers_cleaned[
    "customer_zip_code_prefix"
].dtype)
#checking missing value after coonversion 
print("Missing Values After Conversion:")
print(customers_cleaned.isnull().sum())
#saving the cleaned data into cleaned folder
customers_cleaned.to_csv(
    "Data/cleaned/customers_cleaned.csv",
    index=False
)
#verifying the saved data
customers_verified = pd.read_csv(
    "Data/cleaned/customers_cleaned.csv",
    dtype={"customer_zip_code_prefix": str}
)

print("Saved Dataset Shape:")
print(customers_verified.shape)

print("\nFirst 5 Records:")
print(customers_verified.head())

print("\nPostal Code Data Type:")
print(customers_verified["customer_zip_code_prefix"].dtype)
print("Verified Dataset Shape:")
print(customers_verified.shape)

print("\nMissing Values:")
print(customers_verified.isnull().sum())

print("\nDuplicate Customer IDs:")
print(customers_verified["customer_id"].duplicated().sum())