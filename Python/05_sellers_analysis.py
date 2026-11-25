import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#loading dataset
sellers_df = pd.read_csv(
    "Data/Raw/olist_sellers_dataset.csv"
)
#dataset explore
print("First 5 Records:")
print(sellers_df.head())

print("\nDataset Shape:")
print(sellers_df.shape)

print("\nDataset Columns:")
print(sellers_df.columns)

print("\nDataset Information:")
print(sellers_df.info())
#checking missing values
print("Missing Values:")
print(sellers_df.isnull().sum())
#checking duplicate
print("Full Duplicate Rows:")
print(sellers_df.duplicated().sum())

print("\nDuplicate Seller IDs:")
print(sellers_df["seller_id"].duplicated().sum())
#checking blank values
print("Blank Seller Cities:")
print((sellers_df["seller_city"].str.strip() == "").sum())

print("\nBlank Seller States:")
print((sellers_df["seller_state"].str.strip() == "").sum())
#seller distribution by state
print("Seller Distribution by State:")
print(sellers_df["seller_state"].value_counts())
#calculating seller percenatge
seller_state_percentage = (
    sellers_df["seller_state"].value_counts(normalize=True) * 100
)

print("Seller Percentage by State:")
print(seller_state_percentage.round(2))
#analyzing toop 10 seller cities
seller_city_counts = sellers_df["seller_city"].value_counts()

print("Top 10 Seller Cities:")
print(seller_city_counts.head(10))
#minimum and mzximum postal code  values
print("Minimum Seller Postal Code:")
print(sellers_df["seller_zip_code_prefix"].min())

print("\nMaximum Seller Postal Code:")
print(sellers_df["seller_zip_code_prefix"].max())
#copying the seller data as cleaned and chaning the datatype of poostal code from int to str
sellers_cleaned = sellers_df.copy()

sellers_cleaned["seller_zip_code_prefix"] = (
    sellers_cleaned["seller_zip_code_prefix"]
    .astype(str)
    .str.zfill(5)
)

print("First 10 Seller Postal Codes:")
print(sellers_cleaned["seller_zip_code_prefix"].head(10))

print("\nPostal Code Data Type:")
print(sellers_cleaned["seller_zip_code_prefix"].dtype)
#loading order datset and merging with seller dataset
items_df = pd.read_csv("Data/cleaned/order_items_cleaned.csv")

items_sellers = items_df.merge(
    sellers_cleaned,
    on="seller_id",
    how="left",
    indicator=True,
    validate="many_to_one"
)

print("Order Items Shape:", items_df.shape)
print("Merged Dataset Shape:", items_sellers.shape)

print("\nSeller Matching Results:")
print(items_sellers["_merge"].value_counts())
#saving cleaned seller dataset intoo cleaned folder
sellers_cleaned.to_csv(
    "Data/cleaned/sellers_cleaned.csv",
    index=False
)

print("Cleaned Sellers dataset saved successfully!")
#verifying the saved data
sellers_verified = pd.read_csv(
    "Data/cleaned/sellers_cleaned.csv",
    dtype={"seller_zip_code_prefix": str}
)

print("Verified Dataset Shape:")
print(sellers_verified.shape)

print("\nMissing Values:")
print(sellers_verified.isnull().sum())

print("\nDuplicate Seller IDs:")
print(sellers_verified["seller_id"].duplicated().sum())

print("\nPostal Code Data Type:")
print(sellers_verified["seller_zip_code_prefix"].dtype)

print("\nFirst 5 Records:")
print(sellers_verified.head())