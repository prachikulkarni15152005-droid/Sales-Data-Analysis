import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Order Items dataset
items_df = pd.read_csv(
    "Data/Raw/olist_order_items_dataset.csv"
)

print("ORDER ITEMS DATASET")
print(items_df.head())
#datset shape
print("Dataset Shape:", items_df.shape)
#dataset columns and information
print("Column Names:")
print(items_df.columns)

print("\nDataset Information:")
print(items_df.info())
#checking wether any column contain missing values
print("\nMissing Values:")
print(items_df.isnull().sum())
# Check duplicate full rows
print("\nDuplicate Rows:")
print(items_df.duplicated().sum())
# Check duplicate order-item combinations
print("\nDuplicate Order-Item Combinations:")
print(
    items_df.duplicated(
        subset=["order_id", "order_item_id"]
    ).sum()
)
# Convert shipping_limit_date to datetime
items_df["shipping_limit_date"] = pd.to_datetime(
    items_df["shipping_limit_date"],
    errors="coerce"
)

print("\nUpdated Data Types:")
print(items_df.dtypes)
# Check invalid shipping dates
print("\nInvalid Shipping Dates:")
print(items_df["shipping_limit_date"].isnull().sum())
# Count no of items in each order
items_per_order = items_df.groupby("order_id")["order_item_id"].count()

print("\nItems Per Order:")
print(items_per_order.head())

print("\nItems Per Order Statistics:")
print(items_per_order.describe())
# Distribution of items per order
print("\nOrder Item Count Distribution:")
print(items_per_order.value_counts().sort_index())
# Percentage distribution
print("\nOrder Item Count Percentage:")
print(
    (items_per_order.value_counts(normalize=True).sort_index() * 100)
    .round(2)
)
# Bar chart: Items per order
items_per_order.value_counts().sort_index().plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Distribution of Items per Order")
plt.xlabel("Number of Items")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Product price statistics
print("\nProduct Price Statistics:")
print(items_df["price"].describe())
# Calculate quartiles
Q1 = items_df["price"].quantile(0.25)
Q3 = items_df["price"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate outlier limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Count potential outliers
price_outliers = items_df[
    (items_df["price"] < lower_limit) |
    (items_df["price"] > upper_limit)
]

print("\nPotential Price Outliers:", len(price_outliers))
# Box plot for product prices
plt.figure(figsize=(10, 5))

plt.boxplot(items_df["price"])

plt.title("Product Price Distribution")
plt.ylabel("Price (R$)")
plt.ylim(0, 500)

plt.tight_layout()
plt.show()
# Freight Value Statistics
print("\nFreight Value Statistics:")
print(items_df["freight_value"].describe())
# Calculate quartiles
Q1 = items_df["freight_value"].quantile(0.25)
Q3 = items_df["freight_value"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate outlier limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

# Identify potential outliers
freight_outliers = items_df[
    (items_df["freight_value"] < lower_limit) |
    (items_df["freight_value"] > upper_limit)
]

print("\nPotential Freight Outliers:", len(freight_outliers))
# Count zero freight values
print("\nZero Freight Value Records:")
print((items_df["freight_value"] == 0).sum())
# Box plot for freight value
plt.figure(figsize=(10, 5))

plt.boxplot(items_df["freight_value"])

plt.title("Freight Value Distribution")
plt.ylabel("Freight Value (R$)")

plt.ylim(0, 100)

plt.tight_layout()
plt.show()
# Correlation between product price and freight value
correlation = items_df["price"].corr(
    items_df["freight_value"]
)

print("\nPrice vs Freight Correlation:")
print(correlation)
# Scatter plot: Price vs Freight Value
plt.figure(figsize=(10, 5))

plt.scatter(
    items_df["price"],
    items_df["freight_value"],
    alpha=0.3
)

plt.title("Product Price vs Freight Value")
plt.xlabel("Product Price (R$)")
plt.ylabel("Freight Value (R$)")

plt.tight_layout()
plt.show()
# Check negative product prices
print("\nNegative Product Prices:")
print((items_df["price"] < 0).sum())

# Check negative freight values
print("\nNegative Freight Values:")
print((items_df["freight_value"] < 0).sum())
# Check zero product prices
print("\nZero Product Prices:")
print((items_df["price"] == 0).sum())

# Check zero freight values
print("\nZero Freight Values:")
print((items_df["freight_value"] == 0).sum())
# Validate order item IDs
print("\nZero Order Item IDs:")
print((items_df["order_item_id"] == 0).sum())

print("\nNegative Order Item IDs:")
print((items_df["order_item_id"] < 0).sum())

print("\nMinimum Order Item ID:")
print(items_df["order_item_id"].min())

print("\nMaximum Order Item ID:")
print(items_df["order_item_id"].max())
# Check blank Product IDs
print("\nBlank Product IDs:")
print((items_df["product_id"].str.strip() == "").sum())

# Check blank Seller IDs
print("\nBlank Seller IDs:")
print((items_df["seller_id"].str.strip() == "").sum())
# Shipping limit date range
print("\nEarliest Shipping Limit Date:")
print(items_df["shipping_limit_date"].min())

print("\nLatest Shipping Limit Date:")
print(items_df["shipping_limit_date"].max())
# Load cleaned Orders dataset
orders_df = pd.read_csv(
    "Data/cleaned/orders_cleaned.csv",
    parse_dates=["order_purchase_timestamp"]
)
# Merge order purchase dates with order items
items_orders = items_df.merge(
    orders_df[["order_id", "order_purchase_timestamp",            "order_delivered_carrier_date"]],
    on="order_id",
    how="left",
    validate="many_to_one"
)

# Check unmatched orders
print("\nUnmatched Orders:")
print(items_orders["order_purchase_timestamp"].isnull().sum())
#checking wether shippin date is before purchase date
items_orders["shipping_before_purchase"] = (
    items_orders["shipping_limit_date"] <
    items_orders["order_purchase_timestamp"]
)

print(
    "Shipping Deadline Before Purchase:",
    items_orders["shipping_before_purchase"].sum()
)
#checking the record of highest shipping date
latest_shipping = items_orders[
    items_orders["shipping_limit_date"] ==
    items_orders["shipping_limit_date"].max()
]

print(
    latest_shipping[
        [
            "order_id",
            "product_id",
            "seller_id",
            "order_purchase_timestamp",
            "shipping_limit_date"
        ]
    ].to_string(index=False)
)

#investigating order id:c2bb89b5c1dd978d507284be78a04cb2
print(
    items_orders[
        items_orders["order_id"] ==
        "c2bb89b5c1dd978d507284be78a04cb2"
    ][
        [
            "order_id",
            "order_item_id",
            "product_id",
            "seller_id",
            "shipping_limit_date",
            "price",
            "freight_value",
            "order_purchase_timestamp"
        ]
    ].to_string(index=False)
)
#investigating the above orderid in orders table
print(
    orders_df[
        orders_df["order_id"] ==
        "c2bb89b5c1dd978d507284be78a04cb2"
    ].to_string(index=False)
)
#calculate how many records have a gap greater than one year
shipping_gap = (
    items_orders["shipping_limit_date"] -
    items_orders["order_purchase_timestamp"]
).dt.days

print(
    "Shipping deadlines more than 1 year after purchase:",
    (shipping_gap > 365).sum()
)
#inspect all 4 records which has shipping gap > 1 yr
items_orders["shipping_gap_days"] = (
    items_orders["shipping_limit_date"] -
    items_orders["order_purchase_timestamp"]
).dt.days

unusual_shipping = items_orders[
    items_orders["shipping_gap_days"] > 365
]

print(
    unusual_shipping[
        [
            "order_id",
            "order_item_id",
            "order_purchase_timestamp",
            "shipping_limit_date",
            "shipping_gap_days"
        ]
    ].to_string(index=False)
)
#Check the shipping deadline against carrier handover
items_orders["shipping_after_carrier"] = (
    items_orders["shipping_limit_date"] <
    items_orders["order_delivered_carrier_date"]
)

print(
    "Shipping Deadline Before Carrier Handover:",
    items_orders["shipping_after_carrier"].sum()
)
#calculating Late Shipping Percentage
late_shipping_percentage = (
    items_orders["shipping_after_carrier"].sum()
    / items_orders["order_delivered_carrier_date"].notna().sum()
) * 100

print("Late Shipping Percentage:", round(late_shipping_percentage, 2), "%")
#convertin column to datetime
items_orders["order_delivered_carrier_date"] = pd.to_datetime(
    items_orders["order_delivered_carrier_date"],
    errors="coerce"
)

items_orders["shipping_limit_date"] = pd.to_datetime(
    items_orders["shipping_limit_date"],
    errors="coerce"
)
#calculating shipping_delay_days
items_orders["shipping_delay_days"] = (
    items_orders["order_delivered_carrier_date"] -
    items_orders["shipping_limit_date"]
).dt.total_seconds() / 86400

late_shipping = items_orders[
    items_orders["shipping_delay_days"] > 0
]

print(late_shipping["shipping_delay_days"].describe())
#investigate the 10 most delayed items
top_delayed_items = late_shipping.sort_values(
    by="shipping_delay_days",
    ascending=False
)

print(
    top_delayed_items[
        [
            "order_id",
            "order_item_id",
            "shipping_limit_date",
            "order_delivered_carrier_date",
            "shipping_delay_days"
        ]
    ].head(10).to_string(index=False)
)
#merginig the other columns of the order table with the items table
items_orders = items_df.merge(
    orders_df[
        [
            "order_id",
            "order_purchase_timestamp",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ],
    on="order_id",
    how="left",
    validate="many_to_one"
)
#checking wether custommer delivery is delayed or no
items_orders["customer_delivery_late"] = (
    items_orders["order_delivered_customer_date"] >
    items_orders["order_estimated_delivery_date"]
)

print(
    "Customer Delivery After Estimated Date:",
    items_orders["customer_delivery_late"].sum()
)
#percentage of custoomer delivery delay
customer_delivery_percentage = (
    items_orders["customer_delivery_late"].sum()
    / items_orders["order_delivered_customer_date"].notna().sum()
) * 100

print(
    "Customer Delivery Late Percentage:",
    round(customer_delivery_percentage, 2),
    "%"
)
#converting columns to date time
items_orders["order_delivered_customer_date"] = pd.to_datetime(
    items_orders["order_delivered_customer_date"],
    errors="coerce"
)

items_orders["order_estimated_delivery_date"] = pd.to_datetime(
    items_orders["order_estimated_delivery_date"],
    errors="coerce"
)
#Calculate customer delivery delay in days
items_orders["customer_delay_days"] = (
    items_orders["order_delivered_customer_date"] -
    items_orders["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

late_customer_delivery = items_orders[
    items_orders["customer_delay_days"] > 0
]

print(late_customer_delivery["customer_delay_days"].describe())
#calculating top customers delays
top_customer_delays = late_customer_delivery.sort_values(
    by="customer_delay_days",
    ascending=False
)

print(
    top_customer_delays[
        [
            "order_id",
            "order_item_id",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
            "customer_delay_days"
        ]
    ].head(10).to_string(index=False)
)
#investigate the September 19 pattern
september_deliveries = late_customer_delivery[
    late_customer_delivery["order_delivered_customer_date"].dt.strftime("%Y-%m-%d").isin(
        ["2017-09-19", "2018-09-19"]
    )
]

print(
    september_deliveries[
        [
            "order_id",
            "order_item_id",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
            "customer_delay_days"
        ]
    ].to_string(index=False)
)

print("\nTotal records:", len(september_deliveries))
print(
    "Unique orders:",
    september_deliveries["order_id"].nunique()
)
#checking all the customer delivery dates not just delay dates
print(
    items_orders[
        items_orders["order_delivered_customer_date"].dt.strftime("%Y-%m-%d").isin(
            ["2017-09-19", "2018-09-19"]
        )
    ]["order_id"].nunique()
)
#calculate the minimum and maximum item ID for each order
item_id_check = items_df.groupby("order_id")["order_item_id"].agg(
    ["min", "max", "count"]
)

print(item_id_check.head(10))
#Orders with non-sequential item IDs
item_id_check["expected_count"] = (
    item_id_check["max"] - item_id_check["min"] + 1
)

invalid_item_ids = item_id_check[
    (item_id_check["min"] != 1) |
    (item_id_check["count"] != item_id_check["expected_count"])
]

print("Orders with non-sequential item IDs:")
print(len(invalid_item_ids))
#loading product dataset 
products_df = pd.read_csv(
    "Data/Raw/olist_products_dataset.csv"
)
#finding shape and clumns of the dataset
print("Products Dataset Shape:", products_df.shape)

print("\nProducts Dataset Columns:")
print(products_df.columns)
# Get unique Product IDs from Order Items
order_product_ids = items_df["product_id"].unique()

# Get unique Product IDs from Products
available_product_ids = products_df["product_id"].unique()

# Find Product IDs in Order Items that are missing from Products
missing_products = set(order_product_ids) - set(available_product_ids)

print("Product IDs in Order Items:", len(order_product_ids))
print("Product IDs in Products:", len(available_product_ids))
print("Missing Product IDs:", len(missing_products))
#checking duplicate product ids inn product table
print(
    "Duplicate Product IDs in Products:",
    products_df["product_id"].duplicated().sum()
)
#merge the item table with the product table
items_products = items_df.merge(
    products_df[["product_id", "product_category_name"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

print("Order Items Shape:", items_df.shape)
print("After Products Merge:", items_products.shape)
#check missing product category
print(
    "Missing Product Categories:",
    items_products["product_category_name"].isnull().sum()
)
#verify product_category in products table
print(
    "Missing Categories in Products:",
    products_df["product_category_name"].isnull().sum()
)
#missing_category_products in product table
missing_category_products = products_df[
    products_df["product_category_name"].isnull()
]

print(missing_category_products.head(10))
#it checks how many items where purchased which done have category of the product
missing_product_ids = missing_category_products["product_id"]

purchased_missing_category = items_df[
    items_df["product_id"].isin(missing_product_ids)
]

print(
    "Order Item Records:",
    len(purchased_missing_category)
)

print(
    "Unique Products Purchased:",
    purchased_missing_category["product_id"].nunique()
)
#checking missing values in product table
print("Missing Values in Products Dataset:")
print(products_df.isnull().sum())
#checking the missing value in 4 columns of  the product table
missing_610 = products_df[
    products_df["product_category_name"].isnull()
]

print(
    missing_610[
        [
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty"
        ]
    ].isnull().sum()
)
#checking 4 columns which has missing value row wise(to know the column which dont have category name that row only missing values for other 3 columns) 
missing_all_four = products_df[
    products_df[
        [
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty"
        ]
    ].isnull().all(axis=1)
]

print("Records missing all four columns:", len(missing_all_four))
#checking missing measurements coolumn
missing_measurements = products_df[
    products_df[
        [
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
    ].isnull().any(axis=1)
]

print(missing_measurements.to_string(index=False))

missing_measurement_ids = missing_measurements["product_id"]

measurement_products_purchased = items_df[
    items_df["product_id"].isin(missing_measurement_ids)
]
#find out whether these two products which desnt have measurements data appear in the Order Items dataset.
print("Total Order Item Records:",
      len(measurement_products_purchased))

print("Unique Products:",
      measurement_products_purchased["product_id"].nunique())
#checking duplicate record in product table
print(
    "Duplicate Full Rows in Products:",
    products_df.duplicated().sum()
)
#checking datatype of the columns in product table
print(products_df.dtypes)
#check whether any product has zero or negative values in its physical measurements
measurement_columns = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for column in measurement_columns:
    print(
        f"{column}:",
        (products_df[column] <= 0).sum()
    )
#displaying the products whose weight is less than zeroor eual to zero
invalid_weight = products_df[
    products_df["product_weight_g"] <= 0
]

print(
    invalid_weight[
        [
            "product_id",
            "product_category_name",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
    ].to_string(index=False)
)
#Check whether these four products were purchased(i.e products whose weight is zero)
zero_weight_ids = invalid_weight["product_id"]

zero_weight_purchases = items_df[
    items_df["product_id"].isin(zero_weight_ids)
]

print(
    "Order Item Records:",
    len(zero_weight_purchases)
)

print(
    "Unique Products Purchased:",
    zero_weight_purchases["product_id"].nunique()
)
#check category values
print(
    "Unique Product Categories:",
    products_df["product_category_name"].nunique()
)

print("\nProduct Category Distribution:")
print(
    products_df["product_category_name"].value_counts().head(15)
)
#calculating missing product category percentage
total_products = len(products_df)

missing_category_count = (
    products_df["product_category_name"].isnull().sum()
)

missing_category_percentage = (
    missing_category_count / total_products
) * 100

print("Total Products:", total_products)
print("Missing Categories:", missing_category_count)
print(
    "Missing Category Percentage:",
    round(missing_category_percentage, 2), "%"
)
#loading translation dataset
category_translation_df = pd.read_csv(
    "Data/Raw/product_category_name_translation.csv"
)

print("Translation Dataset Shape:", category_translation_df.shape)

print("\nTranslation Dataset Columns:")
print(category_translation_df.columns)

print("\nFirst 5 Records:")
print(category_translation_df.head())
#checking duplicate and missing values
print("Missing Values:")
print(category_translation_df.isnull().sum())

print(
    "\nDuplicate Portuguese Categories:",
    category_translation_df["product_category_name"].duplicated().sum()
)

print(
    "Duplicate English Categories:",
    category_translation_df["product_category_name_english"].duplicated().sum()
)
#finding untranslated categories
# Get unique product categories
product_categories = set(
    products_df["product_category_name"].dropna().unique()
)

# Get categories available in translation dataset
translated_categories = set(
    category_translation_df["product_category_name"]
)

# Find categories without English translations
untranslated_categories = (
    product_categories - translated_categories
)

# Display results
print("Categories in Products:", len(product_categories))
print("Translated Categories:", len(translated_categories))

print("\nCategories Without Translation:")
print(untranslated_categories)
#mergeing product table with translation table
products_translated = products_df.merge(
    category_translation_df,
    on="product_category_name",
    how="left",
    validate="many_to_one"
)

print("Original Products Shape:", products_df.shape)
print("Translated Products Shape:", products_translated.shape)
#verifying missing english transalation
print(
    "Missing English Translations:",
    products_translated["product_category_name_english"].isnull().sum()
)
#finding missing translation products
missing_translation_products = products_translated[
    products_translated["product_category_name_english"].isnull()
]

print(
    missing_translation_products[
        "product_category_name"
    ].value_counts()
)
#finding missing cateogires name both in english and portuguies
print(
    "Missing Portuguese Categories:",
    products_translated["product_category_name"].isnull().sum()
)

print(
    "Missing English Categories:",
    products_translated["product_category_name_english"].isnull().sum()
)
#displaying newly merged data
print(
    products_translated[
        [
            "product_id",
            "product_category_name",
            "product_category_name_english"
        ]
    ].head(10)
)
#checking duplicate product records in product_translated merge table
print(
    "Duplicate Product IDs:",
    products_translated["product_id"].duplicated().sum()
)

print(
    "Final Dataset Shape:",
    products_translated.shape
)
#checing missing values in product translated
print("Missing Values in Translated Products:")
print(products_translated.isnull().sum())
#copying the dataset as a cleaned dataset
products_cleaned = products_translated.copy()

print("Original Shape:", products_df.shape)
print("Cleaned Shape:", products_cleaned.shape)
#checking duplicates
print(
    "Duplicate Product IDs:",
    products_cleaned["product_id"].duplicated().sum()
)

print(
    "Duplicate Full Rows:",
    products_cleaned.duplicated().sum()
)
#saving the cleaned copy to cleaned data folder
products_cleaned.to_csv(
    "Data/cleaned/products_cleaned.csv",
    index=False
)
#cross checking
products_check = pd.read_csv(
    "Data/cleaned/products_cleaned.csv"
)

print("Saved Dataset Shape:", products_check.shape)
print(products_check.head())
#order dataset copying
items_cleaned = items_df.copy()

print("Original Shape:", items_df.shape)
print("Cleaned Shape:", items_cleaned.shape)
#verifying datatype
print(items_cleaned.dtypes)
#verifying duplication
print(
    "Duplicate Full Rows:",
    items_cleaned.duplicated().sum()
)

print(
    "Duplicate Order Item Combinations:",
    items_cleaned.duplicated(
        subset=["order_id", "order_item_id"]
    ).sum()
)
#saving cleand items datset to cleaned datafolder
items_cleaned.to_csv(
    "Data/cleaned/order_items_cleaned.csv",
    index=False
)
#verifying saved files
items_check = pd.read_csv(
    "Data/cleaned/order_items_cleaned.csv",
    parse_dates=["shipping_limit_date"]
)

print("Saved Dataset Shape:", items_check.shape)
print(items_check.dtypes)
#category_transaltion dataset copy
category_translation_cleaned = category_translation_df.copy()

category_translation_cleaned.to_csv(
    "Data/cleaned/category_translation_cleaned.csv",
    index=False
)
#verifying the datset
translation_check = pd.read_csv(
    "Data/cleaned/category_translation_cleaned.csv"
)

print("Saved Shape:", translation_check.shape)
print(translation_check.head())