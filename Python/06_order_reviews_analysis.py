import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Order Reviews Dataset
reviews_df = pd.read_csv(
    "Data/Raw/olist_order_reviews_dataset.csv"
)

# Display first 5 records
print("First 5 Records:")
print(reviews_df.head())

# Dataset Shape
print("\nDataset Shape:")
print(reviews_df.shape)

# Column Names
print("\nDataset Columns:")
print(reviews_df.columns)

# Dataset Information
print("\nDataset Information:")
print(reviews_df.info())
#calculating missing values
print("Missing Values:")
print(reviews_df.isnull().sum())
#calculating missing review percenatage
missing_percentage = (
    reviews_df.isnull().sum() / len(reviews_df)
) * 100

print("Missing Values Percentage:")
print(missing_percentage.round(2))
# Check complete duplicate rows
print("Duplicate Full Records:")
print(reviews_df.duplicated().sum())

# Check duplicate Review IDs
print("\nDuplicate Review IDs:")
print(reviews_df["review_id"].duplicated().sum())

# Check duplicate Order IDs
print("\nDuplicate Order IDs:")
print(reviews_df["order_id"].duplicated().sum())
#investigating duplicate review ids
duplicate_reviews = reviews_df[
    reviews_df["review_id"].duplicated(keep=False)
]

print("Total Rows with Repeated Review IDs:")
print(duplicate_reviews.shape[0])

print("\nFirst 10 Duplicate Review Records:")
print(
    duplicate_reviews.sort_values("review_id").head(10)
)
#investigate the first repaeted order  id
# Select the first repeated Review ID
sample_review_id = duplicate_reviews["review_id"].iloc[0]

# Display all records with that Review ID
sample_records = reviews_df[
    reviews_df["review_id"] == sample_review_id
]

print("Repeated Review ID:")
print(sample_review_id)

print("\nComplete Records:")
print(sample_records.to_string(index=False))
#investigating review id how many are distinct review ids are duplicated
duplicate_review_id_counts = (
    reviews_df["review_id"].value_counts()
)

repeated_review_id_counts = duplicate_review_id_counts[
    duplicate_review_id_counts > 1
]

print("Number of Distinct Repeated Review IDs:")
print(repeated_review_id_counts.count())

print("\nTotal Repeated Review ID Rows:")
print(repeated_review_id_counts.sum())

print("\nNumber of Review IDs Appearing More Than Twice:")
print((repeated_review_id_counts > 2).sum())

print("\nHighest Review ID Occurrence:")
print(repeated_review_id_counts.max())
#checking duplicate review id and orderid
print(
    duplicate_reviews[
        ["review_id", "order_id"]
    ].head(10)
)
#checking sample review id  wether its order id are same or differnet
sample_review_id = "28642ce6250b94cc72bc85960aec6c62"

print(
    duplicate_reviews[
        duplicate_reviews["review_id"] == sample_review_id
    ][["review_id", "order_id"]]
)
#checking other review ids
print("Total distinct repeated Review IDs:")
print(duplicate_reviews["review_id"].nunique())
#checking particular review id wether Total distinct repeated Review IDs
print("Number of different orders for this Review ID:")
print(sample_records["order_id"].nunique())
#find how many of our 789 repeated Review IDs are associated with multiple orders
orders_per_review = duplicate_reviews.groupby("review_id")["order_id"].nunique()

print(orders_per_review.head(10))
#find out how many of the 789 repeated Review IDs are associated with more than one order
print(
    "Review IDs associated with multiple orders:",
    (orders_per_review > 1).sum()
)
#checking any review id associated with more than 2 order id
print(orders_per_review.value_counts().sort_index())
#reviewing sample review id
print(duplicate_reviews[
    duplicate_reviews["review_id"] == sample_review_id
].to_string(index=False))
#displaying the details of sample review id
print(
    sample_records[
        ["review_score", "review_comment_title", "review_comment_message"]
    ]
)
#checking review score is same or no of same review id
print(sample_records["review_score"].nunique())
#checking review creation dates are same or diff of same review id
print(sample_records["review_creation_date"].nunique())
#checking the answer timestamp are same or differnt
print(sample_records["review_answer_timestamp"].nunique())
#find out whether all 789 repeated Review IDs have identical review details, or whether some have different scores, comments, or timestamps.
review_details = [
    "review_score",
    "review_comment_title",
    "review_comment_message",
    "review_creation_date",
    "review_answer_timestamp"
]
review_detail_counts = (
    duplicate_reviews
    .groupby("review_id")[review_details]
    .nunique(dropna=False)
)

print(review_detail_counts.head(10))
#complete result
print(review_detail_counts.to_string())
#count of identical and differnt reviews
identical_reviews = (
    (review_detail_counts == 1).all(axis=1).sum()
)

different_reviews = (
    (review_detail_counts > 1).any(axis=1).sum()
)

print("Review IDs with identical details:", identical_reviews)
print("Review IDs with different details:", different_reviews)
#display record with duplicate order id
duplicate_order_reviews = reviews_df[
    reviews_df["order_id"].duplicated(keep=False)
]

print(
    duplicate_order_reviews[
        ["order_id", "review_id", "review_score"]
    ].head(10)
)
#reviewing the first order id
sample_order_id = duplicate_order_reviews["order_id"].iloc[0]

sample_order_records = reviews_df[
    reviews_df["order_id"] == sample_order_id
]

print(sample_order_records.to_string(index=False))
#count how many different Review IDs are associated with this sample Order ID
print(sample_order_records["review_id"].nunique())
#check all repeated order ids
reviews_per_order = (
    duplicate_order_reviews
    .groupby("order_id")["review_id"]
    .nunique()
)

print(reviews_per_order.head(10))
#count how many order has reviews 2,3 and mmore
print(reviews_per_order.value_counts().sort_index())
#need to investigate whether the multiple reviews for the same order have identical or different review information.
print(
    sample_order_records[
        [
            "review_id",
            "review_score",
            "review_comment_title",
            "review_comment_message",
            "review_creation_date",
            "review_answer_timestamp"
        ]
    ].nunique(dropna=False)
)
#check wether the above pattern appears for all 547 record
order_review_details = [
    "review_score",
    "review_comment_title",
    "review_comment_message",
    "review_creation_date",
    "review_answer_timestamp"
]

order_detail_counts = (
    duplicate_order_reviews
    .groupby("order_id")[order_review_details]
    .nunique(dropna=False)
)

print(order_detail_counts.head(10))
print(order_detail_counts.to_string(index=False))
#checking the counts of identical and non identical
identical_order_reviews = (
    (order_detail_counts == 1).all(axis=1).sum()
)

different_order_reviews = (
    (order_detail_counts > 1).any(axis=1).sum()
)

print("Orders with identical review details:", identical_order_reviews)
print("Orders with different review details:", different_order_reviews)
#check review score distribution 
review_score_counts = reviews_df["review_score"].value_counts().sort_index()

print("Review Score Counts:")
print(review_score_counts)
#review score percentage
review_score_percentage = (
    reviews_df["review_score"].value_counts(normalize=True).sort_index() * 100
)

print("Review Score Percentage:")
print(review_score_percentage.round(2))
#average review score
average_review_score = reviews_df["review_score"].mean()

print("Average Review Score:", round(average_review_score, 2))
#median review score
median_review_score = reviews_df["review_score"].median()

print("Median Review Score:", median_review_score)
#mode review score
mode_review_score = reviews_df["review_score"].mode()

print("Mode Review Score:")
print(mode_review_score)
#visualization of review score through bar  chart
review_score_counts = reviews_df["review_score"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    review_score_counts.index,
    review_score_counts.values
)

plt.title("Distribution of Customer Review Scores")
plt.xlabel("Review Score")
plt.ylabel("Number of Reviews")
plt.xticks([1, 2, 3, 4, 5])

plt.show()
#loading order datset
orders_df = pd.read_csv("Data/cleaned/orders_cleaned.csv")

print("Orders Dataset Shape:", orders_df.shape)
print("\nOrders Dataset Columns:")
print(orders_df.columns)
#merging the reviews table with the order table
reviews_orders = reviews_df.merge(
    orders_df[["order_id", "order_status"]],
    on="order_id",
    how="left"
)

print("Reviews Dataset Shape:", reviews_df.shape)
print("Merged Dataset Shape:", reviews_orders.shape)
#checking missing values in the reviews_order dataframe
print("Missing Order Status Values:")
print(reviews_orders["order_status"].isnull().sum())
#calculating average review score by status
average_score_by_status = (
    reviews_orders.groupby("order_status")["review_score"].mean()
)

print("Average Review Score by Order Status:")
print(average_score_by_status.round(2))
#calculate num  of reviews by order status
review_count_by_status = (
    reviews_orders.groupby("order_status")["review_score"].count()
)

print("Number of Reviews by Order Status:")
print(review_count_by_status)
#Calculate the percentage distribution of review scores based on status
review_status_percentage = pd.crosstab(
    reviews_orders["order_status"],
    reviews_orders["review_score"],
    normalize="index"
) * 100

print("Review Score Percentage by Order Status:")
print(review_status_percentage.round(2))
#visualize review score by order status
review_status_percentage.plot(
    kind="bar",
    stacked=True,
    figsize=(11, 6)
)

plt.title("Review Score Distribution by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Percentage of Reviews")
plt.legend(title="Review Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#convert columns to date time
reviews_df["review_creation_date"] = pd.to_datetime(
    reviews_df["review_creation_date"]
)

reviews_df["review_answer_timestamp"] = pd.to_datetime(
    reviews_df["review_answer_timestamp"]
)

print(reviews_df[[
    "review_creation_date",
    "review_answer_timestamp"
]].dtypes)
#extracting year from the create date column
reviews_df["review_year"] = (
    reviews_df["review_creation_date"].dt.year
)

print("Reviews by Year:")
print(reviews_df["review_year"].value_counts().sort_index())
#analyzing reviews y month
reviews_df["review_month"] = (
    reviews_df["review_creation_date"].dt.month
)

print("Reviews by Month:")
print(reviews_df["review_month"].value_counts().sort_index())
#display month names instead of number
reviews_df["review_month_name"] = (
    reviews_df["review_creation_date"].dt.month_name()
)

print("Reviews by Month:")
print(
    reviews_df["review_month_name"]
    .value_counts()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)
#visualize monthly review trtends
monthly_review_counts = (
    reviews_df["review_month_name"].value_counts()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
)

plt.figure(figsize=(11, 5))

plt.bar(monthly_review_counts.index, monthly_review_counts.values)

plt.title("Monthly Distribution of Customer Reviews")
plt.xlabel("Month")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
#review response time in days
reviews_df["response_time_days"] = (
    reviews_df["review_answer_timestamp"]
    - reviews_df["review_creation_date"]
).dt.total_seconds() / (24 * 60 * 60)

print("Review Response Time (Days):")
print(reviews_df["response_time_days"].describe())
#identifying unsually long response
Q1 = reviews_df["response_time_days"].quantile(0.25)
Q3 = reviews_df["response_time_days"].quantile(0.75)

IQR = Q3 - Q1

upper_limit = Q3 + (1.5 * IQR)

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Upper Limit:", upper_limit)

response_time_outliers = reviews_df[
    reviews_df["response_time_days"] > upper_limit
]

print("Unusually Long Response Records:", len(response_time_outliers))
#reviewing longest reponse time records
longest_response_times = reviews_df.sort_values(
    by="response_time_days",
    ascending=False
)

print("Top 10 Longest Review Response Times:")

print(
    longest_response_times[
        ["order_id", "review_score",
         "review_creation_date",
         "review_answer_timestamp",
         "response_time_days"]
    ].head(10)
)
#checking negative respoonse timme
negative_response_time = reviews_df[
    reviews_df["response_time_days"] < 0
]

print(
    "Responses Before Review Creation:",
    len(negative_response_time)
)
#check missing values in review datset
print("Missing Values in Reviews Dataset:")
print(reviews_df.isnull().sum())
#create clean review dataset
reviews_cleaned = reviews_df.copy()

print("Original Dataset Shape:", reviews_df.shape)
print("Cleaned Dataset Shape:", reviews_cleaned.shape)
#save the cleaned review dataset
reviews_cleaned.to_csv(
    "Data/cleaned/reviews_cleaned.csv",
    index=False
)

print("Cleaned Reviews Dataset Saved Successfully!")
#verify the cleaned dataset
reviews_check = pd.read_csv(
    "Data/cleaned/reviews_cleaned.csv",
    parse_dates=[
        "review_creation_date",
        "review_answer_timestamp"
    ]
)

print("Saved Dataset Shape:", reviews_check.shape)

print("\nMissing Values:")
print(reviews_check.isnull().sum())

print("\nData Types:")
print(reviews_check.dtypes)