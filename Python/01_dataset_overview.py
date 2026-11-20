import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("Data/Raw/olist_orders_dataset.csv")
# print("First Five Rows")
# print(df.head())
# print(df.shape)
# print(df.columns)
# print("\nDataset Information")
# print(df.info())
# print("\n Count of Missing Valuse")
# print(df.isnull().sum())
# print(df.describe())
# df["order_purchase_timestamp"]=pd.to_datetime(df["order_purchase_timestamp"])
# print(df["order_purchase_timestamp"].dtype)
# df["order_yr"]=df["order_purchase_timestamp"].dt.year
# print(df["order_yr"])
# df["order_month"]=df["order_purchase_timestamp"].dt.month
# df["order_day"]=df["order_purchase_timestamp"].dt.day
# print(df["order_month"])
# print(df["order_day"])
# print(df[["order_purchase_timestamp","order_yr","order_month","order_day"]].head(5))
# df["order_month_name"]=df["order_purchase_timestamp"].dt.month_name()
# print(df["order_month_name"])
# df["order_day_name"]=df["order_purchase_timestamp"].dt.day_name()
# weekday_orders=df["order_day_name"].value_counts()
# print(weekday_orders)
# monthly_order=df["order_month"].value_counts().sort_index()
# print(monthly_order) 

# plt.figure(figsize=(10,5))
# plt.bar(monthly_order.index,monthly_order.values)
# plt.title("Monthly order Trends")
# plt.xlabel("Month")
# plt.ylabel("Number of Orders")
# plt.xticks(range(1,13))
# plt.grid(axis="y",linestyle="--",alpha=0.5)
# plt.show()

# yearly_orders=df["order_yr"].value_counts().sort_index()
# print(yearly_orders)

# plt.figure(figsize=(8,5))
# plt.bar(yearly_orders.index,yearly_orders.values)
# plt.title("yearly order trends")
# plt.xlabel("year")
# plt.ylabel("number of orders")
# plt.grid(axis="y",linestyle="--",alpha=0.5)
# plt.show()

# monthly_yearly_orders=(df.groupby(["order_yr","order_month"])["order_id"].count())
# print(monthly_yearly_orders)

# monthly_comparision=monthly_yearly_orders.unstack(level=0)
# print(monthly_comparision)

# monthly_comparision=monthly_comparision.fillna(0)
# print("\ncleaned data")
# print(monthly_comparision)

# monthly_comparision.plot(kind="bar",figsize=(12,6))
# plt.title("Monthy Orders Comparision by Year")
# plt.xlabel("Month")
# plt.ylabel("number of orders")
# plt.xticks(rotation=45)
# plt.legend(title="year")
# plt.grid(axis="y",linestyle="--",alpha=0.5)
# plt.show()

# print("\n Order Status")
# status_count = df["order_status"].value_counts()
# print(status_count)

# print("\n Status percentage")
# status_percentage = df["order_status"].value_counts(normalize=True)*100
# print(status_percentage)

# status_percentage.plot(kind="barh",figsize=(10,6))
# plt.title("Order Status Analysis")
# plt.xlabel("status_percentage")
# plt.ylabel("order_status")
# plt.grid(axis="y",linestyle="--",alpha=0.5)
# plt.show()

# total_orders=len(df)
# delivered_orders=status_count["delivered"]
# cancelled_orders=status_count["canceled"]
# delivered_percentage=round((delivered_orders/total_orders)*100,2)
# canceled_percentage=round((cancelled_orders/total_orders)*100,2)
# print("\nOrder Percentage KPI's")
# print("total_orders:",total_orders)
# print("delivered_orders:",delivered_orders)
# print("cancelled_orders:",cancelled_orders)
# print("delivered_percentage:",delivered_percentage)
# print("canceled_percentage:",canceled_percentage)

# print(df[[ "order_purchase_timestamp","order_estimated_delivery_date","order_delivered_customer_date"]].dtypes)
# date_columns=["order_purchase_timestamp","order_estimated_delivery_date","order_delivered_customer_date"]
# for column in date_columns:
#     df[column]=pd.to_datetime(df[column])
# print(df[column].dtypes)


# df["delivery_time"]=(df["order_delivered_customer_date"]-df["order_purchase_timestamp"]).dt.days
# print(df["delivery_time"])

# # avg_delivery_time = df["delivery_time"].mean()
# # print("average dellivery time is",round(avg_delivery_time,2),"days")


# # median_delivery_time = df["delivery_time"].median()
# # print("median dellivery time is",round(median_delivery_time,2),"days")

# # fastest_delivery_time = df["delivery_time"].min()
# # slowest_delivery_time = df["delivery_time"].max()
# # print("fastest delivery:",fastest_delivery_time,"days")
# # print("slowest delivery:",slowest_delivery_time,"days")

# print(df["delivery_time"].describe())
# q1=df["delivery_time"].quantile(0.25)
# q3=df["delivery_time"].quantile(0.75)
# iqr=q3-q1
# lower_limit=q1-1.5*iqr
# upper_limit=q3+1.5*iqr
# print("q1:",q1)
# print("q2:",q3)
# print("iqr:",iqr)
# print("lower_limit:",lower_limit)
# print("upper_limit:",upper_limit)

# outliers=df[df["delivery_time"]>upper_limit]
# print("number of outliers orders:",len(outliers))

# outliers_percentage=(len(outliers)/df["delivery_time"].count())*100
# print("outliers percentage is",round(outliers_percentage,2),"%")

# # plt.figure(figsize=(10,6))
# # plt.boxplot(df["delivery_time"].dropna(),vert=False)
# # plt.title("delivery time distribution")
# # plt.ylabel("delivery time(days)")
# # plt.grid(axis="y",linestyle="--",alpha=0.5)
# # plt.show()

# df["delivery_status"]=(df["order_delivered_customer_date"]>df["order_estimated_delivery_date"])
# print(df["delivery_status"].head(10))

# delivery_status_count=df["delivery_status"].value_counts()
# print(delivery_status_count)

# import numpy as np
# df["corrected_delivery_status"]=np.where(
#     df["order_delivered_customer_date"].isna(),
#                                    "not delivered",
#              np.where(
#                  df["order_delivered_customer_date"]>df["order_estimated_delivery_date"],
#                  "late",
#                  "on time"
#              )
# )
# print(df["corrected_delivery_status"].value_counts())

# total_deliverables=((df["corrected_delivery_status"]=="on time").sum()+
#                     (df["corrected_delivery_status"]=="late").sum())
# ontime_percentage=((df["corrected_delivery_status"]=="on time").sum()/total_deliverables)*100
# late_percentage=((df["corrected_delivery_status"]=="late").sum()/total_deliverables)*100
# print("on time percentage is :",round(ontime_percentage,2),"%")
# print("late percentage is :",round(late_percentage,2),"%")

# delivery_counts = df["corrected_delivery_status"].value_counts()
# delivery_counts.plot(kind="bar",figsize=(9,5))
# plt.title("Delivery Status Distribution")
# plt.xlabel("Delivery Status")
# plt.ylabel("Number of orders")
# plt.xticks(rotation = 0)
# plt.grid(axis="y",linestyle="--",alpha=0.5)
# plt.show()

# print("Duplicate Record Analysis")
# duplicate_count = df.duplicated().sum()
# print("Total duplicate rows:",duplicate_count)

# duplicate_order_ids=df["order_id"].duplicated().sum()
# print("Duplicate Order Ids:",duplicate_order_ids)

# missing_values=df.isnull().sum()
# missing_percentage=(missing_values/len(df))*100
# print("Missing Values:",missing_values)
# print("\nMissing Percentage:",missing_percentage)

# missing_delivery_by_status=(df.groupby("order_status")
# ["order_delivered_customer_date"].apply(
#     lambda x:x.isnull().sum()
# )
# )
# print(missing_delivery_by_status)

# delivered_missing_dates=df[(df["order_status"]=="delivered")&(df["order_delivered_customer_date"].isnull())]
# print(delivered_missing_dates)

# print(delivered_missing_dates[
#     ["order_id",
#      "order_purchase_timestamp",
#      "order_approved_at",
#      "order_delivered_carrier_date",
#      "order_delivered_customer_date",
#      "order_estimated_delivery_date"]
# ].to_string(index=False))

# print(
#     delivered_missing_dates[
#         [
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date"
#     ]].isnull().sum())

missing_approval_by_status=(df.groupby("order_status")
    ["order_approved_at"].apply(
        lambda x:x.isnull().sum()
    )
)
print(missing_approval_by_status)

delivered_missing_approval=df[(df["order_status"]=="delivered")&(df["order_approved_at"].isnull())]
print(
    delivered_missing_approval[
        [
            "order_id",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ].to_string(index=False)
)

payments_df = pd.read_csv(
    "Data/Raw/olist_order_payments_dataset.csv"
)

print(payments_df.head())

payments_record_for_14=payments_df[
    payments_df["order_id"].isin(
        delivered_missing_approval["order_id"])
]
print(payments_record_for_14)

# Data Quality Observation:
# 14 delivered orders have missing order_approved_at timestamps.
# All 14 orders have corresponding payment records.
# Their actual delivery dates are available.
# Approval timestamps cannot be recovered from the payment records.
# Therefore, preserve the missing values instead of guessing.

# missing_values=df.isnull().sum()
# missinng_percentage=((missing_values/len(df))*100).round(2)
# missing_summary=pd.DataFrame({
#     "missing_values":missing_values,
#     "missing_percentage":missinng_percentage
# })
# print(missing_summary)

# invalid_delivery_date=df[
#     df["order_purchase_timestamp"]>
#     df["order_delivered_customer_date"]]
# print("Invalid delivery date:",len(invalid_delivery_date))

# invalid_carrier_dates = df[
#     df["order_delivered_carrier_date"] <
#     df["order_purchase_timestamp"]
# ]
# print("Invalid carrier date records:", len(invalid_carrier_dates))

# print(
#     invalid_carrier_dates[
#         [
#             "order_id",
#             "order_purchase_timestamp",
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date"
#         ]
#     ].to_string(index=False)
# )



# print(invalid_carrier_dates[
#     [
#         "order_purchase_timestamp",
#         "order_delivered_carrier_date"
#     ]
# ].dtypes)



# invalid_carrier_dates = invalid_carrier_dates.copy()

# invalid_carrier_dates["order_purchase_timestamp"] = pd.to_datetime(
#     invalid_carrier_dates["order_purchase_timestamp"]
# )

# invalid_carrier_dates["order_delivered_carrier_date"] = pd.to_datetime(
#     invalid_carrier_dates["order_delivered_carrier_date"]
# )

# invalid_carrier_dates["time_difference"] = (
#     invalid_carrier_dates["order_purchase_timestamp"] -
#     invalid_carrier_dates["order_delivered_carrier_date"]
# )

# print(invalid_carrier_dates["time_difference"].describe())


# largest_time_difference=invalid_carrier_dates.sort_values(
#     by="time_difference",
#     ascending=False
# )
# print(largest_time_difference[
#     [
#         "order_id",
#         "order_purchase_timestamp",
#         "order_delivered_carrier_date",
#         "time_difference"
#     ]
# ].head(10).to_string(index=False))

# extreme_order = df[
#     df["order_id"] == "7c48bb55e8e4f7e56d412e9653db37bc"
# ]

# print(
#     extreme_order[
#         [
#             "order_id",
#             "order_status",
#             "order_purchase_timestamp",
#             "order_approved_at",
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date",
#             "order_estimated_delivery_date"
#         ]
#     ].to_string(index=False)
# )

# large_time_difference_greaterthan1day=invalid_carrier_dates[
#     invalid_carrier_dates["time_difference"]>pd.Timedelta(days=1)
# ]
# print("records with differnce greater than one day:",len(large_time_difference_greaterthan1day))

# print(
#     large_time_difference_greaterthan1day[
#         [
#             "order_id",
#             "order_status",
#             "order_purchase_timestamp",
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date",
#             "time_difference"
#         ]
#     ].to_string(index=False)
# )
# Data Quality Observation:
# 166 orders have carrier timestamps earlier than purchase timestamps.
# 164 records have differences of one day or less.
# 2 records have differences greater than one day.
# These timestamps are chronologically inconsistent.
# Original values are preserved because the correct timestamps are unknown.

# invalid_estimated_dates = df[
#     df["order_delivered_customer_date"] >
#     df["order_estimated_delivery_date"]
# ]

# print("Orders delivered after estimated dates:", len(invalid_estimated_dates))

# print(
#     "Missing estimated delivery dates:",
#     df["order_estimated_delivery_date"].isnull().sum()
# )

# invalid_carrier_delivery_dates = df[
#     df["order_delivered_carrier_date"] >
#     df["order_delivered_customer_date"]
# ]

# print(
#     "Carrier date after customer delivery:",
#     len(invalid_carrier_delivery_dates)
# )

# print(
#     invalid_carrier_delivery_dates[
#         [
#             "order_id",
#             "order_status",
#             "order_purchase_timestamp",
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date"
#         ]
#     ].to_string(index=False)
# )

# invalid_carrier_delivery_dates["order_delivered_customer_date"] = pd.to_datetime(
#     invalid_carrier_delivery_dates["order_delivered_customer_date"]
# )

# invalid_carrier_delivery_dates["order_delivered_carrier_date"] = pd.to_datetime(
#     invalid_carrier_delivery_dates["order_delivered_carrier_date"]
# )
# invalid_carrier_delivery_dates = invalid_carrier_delivery_dates.copy()

# invalid_carrier_delivery_dates["carrier_delivery_gap"] = (
#     invalid_carrier_delivery_dates["order_delivered_carrier_date"] -
#     invalid_carrier_delivery_dates["order_delivered_customer_date"]
# )

# print(invalid_carrier_delivery_dates["carrier_delivery_gap"].describe())

# Data Quality Observation:
# 23 orders have carrier timestamps later than customer delivery timestamps.
# The average time difference is approximately 3.27 days.
# The maximum time difference is approximately 16.10 days.
# These records violate the expected delivery sequence.
# Original timestamps are preserved because the correct values are unknown.

# invalid_approval_dates = df[
#     df["order_approved_at"] <
#     df["order_purchase_timestamp"]
# ]

# print("Approval date before purchase:", len(invalid_approval_dates))

# invalid_approval_carrier_dates = df[
#     df["order_delivered_carrier_date"] <
#     df["order_approved_at"]
# ]

# print(
#     "Carrier date before approval:",
#     len(invalid_approval_carrier_dates)
# )

# print(
#     invalid_approval_carrier_dates[
#         [
#             "order_id",
#             "order_status",
#             "order_purchase_timestamp",
#             "order_approved_at",
#             "order_delivered_carrier_date",
#             "order_delivered_customer_date"
#         ]
#     ].head(10).to_string(index=False)
# )

# invalid_approval_carrier_dates["order_approved_at"] = pd.to_datetime(
#     invalid_approval_carrier_dates["order_approved_at"]
# )

# invalid_approval_carrier_dates["order_delivered_carrier_date"] = pd.to_datetime(
#     invalid_approval_carrier_dates["order_delivered_carrier_date"])

# invalid_approval_carrier_dates = (
#     invalid_approval_carrier_dates.copy()
# )

# invalid_approval_carrier_dates["approval_carrier_gap"] = (
#     invalid_approval_carrier_dates["order_approved_at"] -
#     invalid_approval_carrier_dates["order_delivered_carrier_date"]
# )

# print(
#     invalid_approval_carrier_dates[
#         "approval_carrier_gap"
#     ].describe()
# )
# largest_approval_gaps = invalid_approval_carrier_dates.sort_values(
#     by="approval_carrier_gap",
#     ascending=False
# )

# print(
#     largest_approval_gaps[
#         [
#             "order_id",
#             "order_approved_at",
#             "order_delivered_carrier_date",
#             "approval_carrier_gap"
#         ]
#     ].head(10).to_string(index=False)
# )
# approval_gaps_over_one_day = invalid_approval_carrier_dates[
#     invalid_approval_carrier_dates["approval_carrier_gap"] >
#     pd.Timedelta(days=1)
# ]

# print(
#     "Records with approval-carrier gap greater than 1 day:",
#     len(approval_gaps_over_one_day)
# )
# Data Quality Observation:
# 1,359 orders have carrier timestamps before approval timestamps.
# 901 records have differences of one day or less.
# 458 records have differences greater than one day.
# One record has an exceptionally large difference of approximately 171 days.
# Original timestamps are preserved without guessing replacement values.

invalid_approval_delivery_dates = df[
    df["order_delivered_customer_date"] <
    df["order_approved_at"]
]

print(
    "Customer delivery before approval:",
    len(invalid_approval_delivery_dates)
)
invalid_approval_delivery_dates["order_approved_at"] = pd.to_datetime(
    invalid_approval_delivery_dates["order_approved_at"]
)

invalid_approval_delivery_dates["order_delivered_customer_date"] = pd.to_datetime(
    invalid_approval_delivery_dates["order_delivered_customer_date"])

invalid_approval_delivery_dates = (
    invalid_approval_delivery_dates.copy()
)

invalid_approval_delivery_dates["approval_delivery_gap"] = (
    invalid_approval_delivery_dates["order_approved_at"] -
    invalid_approval_delivery_dates["order_delivered_customer_date"]
)

# print(
#     invalid_approval_delivery_dates[
#         "approval_delivery_gap"
#     ].describe()
# )
# Data Quality Observation:
# 61 orders have customer delivery timestamps before approval timestamps.
# Average difference is approximately 1 day and 15 hours.
# Maximum difference is approximately 6 days and 23 hours.
# These records violate the expected order timeline.
# Original timestamps are preserved without guessing replacement values.

print(
    "Missing approval timestamps in these records:",
    invalid_approval_delivery_dates["order_approved_at"].isnull().sum()
)

# Additional Validation:
# All 61 records have non-missing approval timestamps.
# All 61 records have non-missing customer delivery timestamps.
# Therefore, the chronological inconsistency is not caused by missing values.
invalid_approval_estimated_dates = df[
    df["order_approved_at"] >
    df["order_estimated_delivery_date"]
]

print(
    "Approval date after estimated delivery:",
    len(invalid_approval_estimated_dates)
)
print(
    invalid_approval_estimated_dates[
        [
            "order_id",
            "order_status",
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_customer_date",
            "order_estimated_delivery_date"
        ]
    ].to_string(index=False)
)
invalid_approval_estimated_dates["order_approved_at"] = pd.to_datetime(
    invalid_approval_estimated_dates["order_approved_at"]
)

invalid_approval_estimated_dates["order_estimated_delivery_date"] = pd.to_datetime(
    invalid_approval_estimated_dates["order_estimated_delivery_date"])

invalid_approval_estimated_dates = (
    invalid_approval_estimated_dates.copy()
)

invalid_approval_estimated_dates["approval_estimated_gap"] = (
    invalid_approval_estimated_dates["order_approved_at"] -
    invalid_approval_estimated_dates["order_estimated_delivery_date"]
)

print(
    invalid_approval_estimated_dates[
        "approval_estimated_gap"
    ].describe()
)

# Data Quality Observation:
# 12 orders have approval timestamps later than estimated delivery dates.
# The average difference is approximately 15 days and 19 hours.
# The maximum difference is approximately 145 days and 15 hours.
# These records have chronologically inconsistent timestamps.
# Original timestamps are preserved because the correct values are unknown.

