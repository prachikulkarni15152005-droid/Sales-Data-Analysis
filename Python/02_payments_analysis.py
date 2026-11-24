import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Payments dataset
payments_df = pd.read_csv(
    "Data/Raw/olist_order_payments_dataset.csv"
)

# Display first five records
print("PAYMENTS DATASET")
print(payments_df.head())
#check the shape of the dataset
print("Dataset Shape:", payments_df.shape)
#check column names
print("\nColumn Names:")
print(payments_df.columns)
#check dataset information
print("\nDataset Information:")
payments_df.info()
#checking null values in the  dataset
print("Missing Values:")
print(payments_df.isnull().sum())
#payment methods
print("Payment Method Distribution:")
print(payments_df["payment_type"].value_counts())
print(payments_df["payment_type"].unique())
#calculate payment method percentage
payment_percentage = (
    payments_df["payment_type"]
    .value_counts(normalize=True) * 100
)

print("Payment Method Percentage:")
print(payment_percentage.round(2))
#visualize payment method distribution
payment_counts = payments_df["payment_type"].value_counts()

plt.figure(figsize=(8, 5))

payment_counts.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Payments")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#calculate descriptive statistics
print("Payment Value Statistics:")
print(payments_df["payment_value"].describe())
#check zero value payments
zero_payments = payments_df[
    payments_df["payment_value"] == 0
]

print("Zero-value payment records:", len(zero_payments))

print("\nZero-value payment details:")
print(zero_payments.head())
#count of zero payment records
print("Total zero-value payments:", len(zero_payments))
#payment methods of 0 payment records
print("Payment types of zero-value records:")
print(zero_payments["payment_type"].value_counts())
#inspect all zero payment rcords
print(zero_payments)
#investigating specific record which appeard twice
specific_order = payments_df[
    payments_df["order_id"] ==
    "fa65dad1b0e818e3ccc5cb0e39231352"
]

print(specific_order)
#check duplicate records
print(
    "Total duplicate rows:",
    payments_df.duplicated().sum()
)
#check duplicate payment identifiers
print(
    "Duplicate order_id and payment_sequential combinations:",
    payments_df.duplicated(
        subset=["order_id", "payment_sequential"]
    ).sum()
)
#check payment installments
print("Payment Installment Distribution:")
print(payments_df["payment_installments"].value_counts().sort_index())
#calculate installment percentage
installment_percentage = (
    payments_df["payment_installments"]
    .value_counts(normalize=True)
    .sort_index() * 100
)

print("Installment Percentage Distribution:")
print(installment_percentage.round(2))
#investigating 0 installment records
zero_installments = payments_df[
    payments_df["payment_installments"] == 0
]

print("Zero-installment records:")
print(zero_installments)
#payment type of  0 installment records
print("\nPayment types:")
print(zero_installments["payment_type"].value_counts())
#payment value outlier detection using IQR method
Q1 = payments_df["payment_value"].quantile(0.25)

Q3 = payments_df["payment_value"].quantile(0.75)

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
#calculating upper and lower limit
upper_limit = Q3 + (1.5 * IQR)

lower_limit = Q1 - (1.5 * IQR)

print("Upper Limit:", upper_limit)
print("Lower Limit:", lower_limit)
#identifying outlier records
payment_outliers = payments_df[
    payments_df["payment_value"] > upper_limit
]

print("Total payment outliers:", len(payment_outliers))

print("\nOutlier records:")
print(payment_outliers.head())
#calculate the number and % of outliers
total_outliers = len(payment_outliers)

outlier_percentage = (
    total_outliers / len(payments_df)
) * 100

print("Total Payment Outliers:", total_outliers)

print("Outlier Percentage:", round(outlier_percentage, 2), "%")
#visualize payment value outliers
plt.figure(figsize=(8, 5))

plt.boxplot(payments_df["payment_value"])

plt.title("Payment Value Outlier Detection")
plt.ylabel("Payment Value (R$)")

plt.tight_layout()
plt.show()
#zoomed boxplot
plt.figure(figsize=(8, 5))

plt.boxplot(payments_df["payment_value"])

plt.title("Payment Value Distribution (Zoomed)")
plt.ylabel("Payment Value (R$)")

plt.ylim(0, 500)

plt.tight_layout()
plt.show()
#visualization of the payment value using histogram
plt.figure(figsize=(8, 5))

plt.hist(
    payments_df["payment_value"],
    bins=50,
    edgecolor="black"
)

plt.title("Distribution of Payment Values")
plt.xlabel("Payment Value (R$)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
#updated range of the histogram
plt.figure(figsize=(8, 5))

plt.hist(
    payments_df["payment_value"],
    bins=50,
    range=(0, 1000),
    edgecolor="black"
)

plt.title("Distribution of Payment Values (0–1000)")
plt.xlabel("Payment Value (R$)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
#Calculate payment statistics by payment method
payment_method_analysis = payments_df.groupby(
    "payment_type"
)["payment_value"].agg(
    ["count", "sum", "mean", "median"]
)

print("Payment Value Analysis by Payment Method:")
print(payment_method_analysis.round(2))
#average payment value by payment method
plt.figure(figsize=(8, 5))

payment_method_analysis["mean"].plot(kind="bar")

plt.title("Average Payment Value by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Average Payment Value (R$)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#calculate total payments per record
order_payment = payments_df.groupby("order_id").agg(
    total_payment=("payment_value", "sum"),
    number_of_payments=("payment_sequential", "count")
)

print("Order-Level Payment Analysis:")
print(order_payment.head())
#understanding how many order have multiple payments
print("Payment Count Distribution:")
print(order_payment["number_of_payments"].value_counts().sort_index())
#calcualte percentage distribution
payment_count_percentage = (
    order_payment["number_of_payments"]
    .value_counts(normalize=True)
    .sort_index() * 100
)

print("Payment Count Percentage:")
print(payment_count_percentage.round(2))
#identifying orders with multiple payment 
multiple_payment_orders = order_payment[
    order_payment["number_of_payments"] > 1
]

print("Orders with multiple payments:")
print(multiple_payment_orders.head())

print("Total orders with multiple payments:",
      multiple_payment_orders.shape[0])

#order_id which has 6 payment records(investigating)
print(payments_df[
    payments_df["order_id"] == "009ac365164f8e06f59d18a08045f6c4"
])

print(
    payments_df[
        payments_df["order_id"] == "009ac365164f8e06f59d18a08045f6c4"
    ][["payment_sequential", "payment_type", "payment_value"]]
)
#analyzing how many orders use more than one type of payment method
payment_methods_per_order = payments_df.groupby(
    "order_id"
)["payment_type"].nunique()

print("Orders using multiple payment methods:")
print((payment_methods_per_order > 1).sum())
#Find the most common payment method combinations
payment_combinations = payments_df.groupby(
    "order_id"
)["payment_type"].apply(
    lambda x: " + ".join(sorted(set(x)))
)

print(
    payment_combinations.value_counts().head(10)
)
#Calculate payment method combination percentages
payment_combination_percentage = (
    payment_combinations.value_counts(normalize=True) * 100
)

print(payment_combination_percentage.round(2))
#Visualize payment combinations
plt.figure(figsize=(10, 5))

payment_combinations.value_counts().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Order Distribution by Payment Method Combination")
plt.xlabel("Number of Orders")
plt.ylabel("Payment Method Combination")

plt.tight_layout()
plt.show()
#orders with more than 5 payment records
high_payment_orders = order_payment[
    order_payment["number_of_payments"] > 5
]

print("Orders with more than 5 payment records:")
print(high_payment_orders.sort_values(
    by="number_of_payments",
    ascending=False
).head(10))

print("Total:", high_payment_orders.shape[0])
#investigate the order with 26 payment records
unusual_order_id = "ccf804e764ed5650cd8759557269dc13"

print(
    payments_df[
        payments_df["order_id"] == unusual_order_id
    ].sort_values("payment_sequential")
)
print(
    payments_df[
        payments_df["order_id"] == unusual_order_id
    ][["payment_sequential", "payment_type", "payment_value"]]
    .to_string(index=False)
)
#checking wether payment value is negativve or no 
print("Negative payment values:")
print((payments_df["payment_value"] < 0).sum())
#check zero payment records
zero_payments = payments_df[
    payments_df["payment_value"] == 0
]

print("Zero payment records:", zero_payments.shape[0])

print(
    zero_payments[
        ["order_id", "payment_type", "payment_installments", "payment_value"]
    ].to_string(index=False)
)
#checking records with -ve installments
print("Negative installment records:")
print((payments_df["payment_installments"] < 0).sum())
#records of zero installments
zero_installments = payments_df[
    payments_df["payment_installments"] == 0
]

print("Zero installment records:", zero_installments.shape[0])

print(
    zero_installments[
        ["order_id", "payment_type", "payment_installments", "payment_value"]
    ].to_string(index=False)
)
#min and max installments
print("Minimum installments:",
      payments_df["payment_installments"].min())

print("Maximum installments:",
      payments_df["payment_installments"].max())
#checking datatypes
print(payments_df[[
    "payment_sequential",
    "payment_installments",
    "payment_value"
]].dtypes)
#check whether payments sequntial value is either 0 or negative
print("Zero payment sequence records:",
      (payments_df["payment_sequential"] == 0).sum())

print("Negative payment sequence records:",
      (payments_df["payment_sequential"] < 0).sum())
#checking duplicate order id and payment sequential
print(
    "Duplicate order and payment sequence combinations:",
    payments_df.duplicated(
        subset=["order_id", "payment_sequential"]
    ).sum()
)
# Create a cleaned copy of the Payments dataset
payments_cleaned = payments_df.copy()
print("original dataset:",payments_df.shape)
print("cleaned copy:",payments_cleaned.shape)
#verifying missing values and duplicate records in the cleaned dataset
print("Missing values:")
print(payments_cleaned.isnull().sum())

print("\nDuplicate rows:")
print(payments_cleaned.duplicated().sum())

print("\nDuplicate order-payment combinations:")
print(
    payments_cleaned.duplicated(
        subset=["order_id", "payment_sequential"]
    ).sum()
)
#save the cleaned dataset
payments_cleaned.to_csv(
    "Data/cleaned/payments_cleaned.csv",
    index=False
)
#cross  check of the  copiied dataset
payments_check = pd.read_csv(
    "Data/cleaned/payments_cleaned.csv"
)

print(payments_check.shape)
print(payments_check.head())