import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Geolocation Dataset
geolocation_df = pd.read_csv(
    "Data/Raw/olist_geolocation_dataset.csv"
)

# Display first 5 records
print("First 5 Records:")
print(geolocation_df.head())

# Display dataset shape
print("\nGeolocation Dataset Shape:")
print(geolocation_df.shape)

# Display column names
print("\nGeolocation Dataset Columns:")
print(geolocation_df.columns)
# Dataset information
print("\nDataset Information:")
print(geolocation_df.info())

# Statistical summary
print("\nStatistical Summary:")
print(geolocation_df.describe())
#identifying any missing values
print("Missing Values:")
print(geolocation_df.isnull().sum())
# Check complete duplicate records
duplicate_rows = geolocation_df.duplicated().sum()

print("Total Duplicate Rows:", duplicate_rows)
# Count repeated postal-code prefixes
duplicate_zip_codes = geolocation_df[
    geolocation_df["geolocation_zip_code_prefix"].duplicated()
]

print(
    "Repeated Postal Code Records:",
    len(duplicate_zip_codes)
)

print(
    "\nUnique Repeated Postal Codes:",
    duplicate_zip_codes["geolocation_zip_code_prefix"].nunique()
)
# Count unique coordinate combinations per postal code
coordinates_per_zip = (
    geolocation_df.groupby("geolocation_zip_code_prefix")
    [["geolocation_lat", "geolocation_lng"]]
    .apply(lambda x: x.drop_duplicates().shape[0])
)

print("Maximum Unique Coordinates for One Postal Code:")
print(coordinates_per_zip.max())

print("\nPostal Codes with More Than One Coordinate:")
print((coordinates_per_zip > 1).sum())
# Find postal code with maximum unique coordinates
max_coordinates_zip = coordinates_per_zip.idxmax()

print("Postal Code with Maximum Coordinates:")
print(max_coordinates_zip)

print("\nNumber of Unique Coordinates:")
print(coordinates_per_zip.max())
# Filter records for postal code 38400
zip_38400 = geolocation_df[
    geolocation_df["geolocation_zip_code_prefix"] == 38400
]

print("Records for Postal Code 38400:")
print(zip_38400.head(10))

print("\nTotal Records:")
print(len(zip_38400))

print("\nUnique Coordinate Combinations:")
print(
    zip_38400[
        ["geolocation_lat", "geolocation_lng"]
    ].drop_duplicates().shape[0]
)
# Check unique cities and states for postal code 38400
print("Unique Cities:")
print(zip_38400["geolocation_city"].unique())

print("\nUnique States:")
print(zip_38400["geolocation_state"].unique())

print("\nCity Counts:")
print(zip_38400["geolocation_city"].value_counts())
# Count unique city names
unique_cities = geolocation_df["geolocation_city"].nunique()

print("Total Unique City Names:", unique_cities)

# Display the 20 most frequent city names
print("\nTop 20 Cities:")
print(geolocation_df["geolocation_city"].value_counts().head(20))
# Count unique states
unique_states = geolocation_df["geolocation_state"].nunique()

print("Total Unique States:", unique_states)

print("\nState Counts:")
print(geolocation_df["geolocation_state"].value_counts())
# Check latitude outside Brazil's approximate range
invalid_latitude = geolocation_df[
    (geolocation_df["geolocation_lat"] < -34) |
    (geolocation_df["geolocation_lat"] > 6)
]

# Check longitude outside Brazil's approximate range
invalid_longitude = geolocation_df[
    (geolocation_df["geolocation_lng"] < -74) |
    (geolocation_df["geolocation_lng"] > -34)
]

print("Records with Invalid Latitude:", len(invalid_latitude))

print("Records with Invalid Longitude:", len(invalid_longitude))
# Display records with unusual latitude
print("Records with Unusual Latitude:")
print(invalid_latitude.head(10))

# Display records with unusual longitude
print("\nRecords with Unusual Longitude:")
print(invalid_longitude.head(10))
# Combine latitude and longitude anomaly conditions
invalid_coordinates = geolocation_df[
    (geolocation_df["geolocation_lat"] < -34) |
    (geolocation_df["geolocation_lat"] > 6) |
    (geolocation_df["geolocation_lng"] < -74) |
    (geolocation_df["geolocation_lng"] > -34)
]

print("Total Records with Unusual Coordinates:")
print(len(invalid_coordinates))
# Count unique cities associated with each postal code
cities_per_zip = (
    geolocation_df.groupby("geolocation_zip_code_prefix")[
        "geolocation_city"
    ].nunique()
)

print("Maximum Cities for One Postal Code:")
print(cities_per_zip.max())

print("\nPostal Codes Associated with Multiple Cities:")
print((cities_per_zip > 1).sum())
# Find postal code associated with the maximum number of cities
max_cities_zip = cities_per_zip.idxmax()

print("Postal Code with Maximum Cities:")
print(max_cities_zip)

print("\nNumber of Different City Names:")
print(cities_per_zip.max())
# Filter records for postal code 6900
zip_6900 = geolocation_df[
    geolocation_df["geolocation_zip_code_prefix"] == 6900
]

# Display unique city names
print("Unique Cities:")
print(zip_6900["geolocation_city"].unique())

# Display unique states
print("\nUnique States:")
print(zip_6900["geolocation_state"].unique())

# Count records for each city
print("\nCity Counts:")
print(zip_6900["geolocation_city"].value_counts())
# Count unique states associated with each postal code
states_per_zip = (
    geolocation_df.groupby("geolocation_zip_code_prefix")[
        "geolocation_state"
    ].nunique()
)

print("Maximum States for One Postal Code:")
print(states_per_zip.max())

print("\nPostal Codes Associated with Multiple States:")
print((states_per_zip > 1).sum())
# Find postal codes associated with more than one state
multiple_state_zips = states_per_zip[states_per_zip > 1]

print("Postal Codes Associated with Multiple States:")
print(multiple_state_zips)
multiple_state_records = geolocation_df[
    geolocation_df["geolocation_zip_code_prefix"].isin(
        multiple_state_zips.index
    )
]

state_combinations = (
    multiple_state_records.groupby("geolocation_zip_code_prefix")[
        "geolocation_state"
    ].unique()
)
print("States Associated with Each Postal Code:")
print(state_combinations)
#finding the details of the postal code
print(
    multiple_state_records.sort_values(
        "geolocation_zip_code_prefix"
    )
)
#inspect only the state combinations
state_record_counts = (
    multiple_state_records.groupby(
        ["geolocation_zip_code_prefix", "geolocation_state"]
    ).size()
)

print("Record Counts by Postal Code and State:")
print(state_record_counts)
#data type of the postal code
print("Postal Code Data Type:")
print(geolocation_df["geolocation_zip_code_prefix"].dtype)
#changing the postal code datatype to string
geolocation_cleaned = geolocation_df.copy()

geolocation_cleaned["geolocation_zip_code_prefix"] = (
    geolocation_cleaned["geolocation_zip_code_prefix"]
    .astype(str)
    .str.zfill(5)
)

print("Postal Code Data Type:")
print(geolocation_cleaned["geolocation_zip_code_prefix"].dtype)

print("\nFirst 10 Postal Codes:")
print(geolocation_cleaned["geolocation_zip_code_prefix"].head(10))
#checking duplicate records
print("Duplicate Rows in Geolocation Dataset:")
print(geolocation_cleaned.duplicated().sum())
#inspect exact duplicates
duplicate_records = geolocation_cleaned[
    geolocation_cleaned.duplicated(keep=False)
]

print("Total Rows Belonging to Duplicate Groups:")
print(len(duplicate_records))

print("\nFirst 10 Duplicate Records:")
print(duplicate_records.head(10))
#checking duplicate counts
geolocation_cleaned_no_duplicates = (
    geolocation_cleaned.drop_duplicates()
)

print("Original Cleaned Dataset Shape:")
print(geolocation_cleaned.shape)

print("\nShape After Removing Exact Duplicates:")
print(geolocation_cleaned_no_duplicates.shape)

print("\nRemaining Duplicate Rows:")
print(geolocation_cleaned_no_duplicates.duplicated().sum())
#checking unique postal codes after removing duplicates
print("Unique Postal Codes:")
print(
    geolocation_cleaned_no_duplicates[
        "geolocation_zip_code_prefix"
    ].nunique()
)
#checking how many records for each postal code
records_per_zip = (
    geolocation_cleaned_no_duplicates
    .groupby("geolocation_zip_code_prefix")
    .size()
)

print("Maximum Records for One Postal Code:")
print(records_per_zip.max())

print("\nPostal Codes with Multiple Records:")
print((records_per_zip > 1).sum())
#postal code with maximum records
print("Postal Code with Maximum Records:")
print(records_per_zip.idxmax())

print("\nMaximum Number of Records:")
print(records_per_zip.max())
#verifying coordinate combinations after removing duplicates
zip_38400_cleaned = geolocation_cleaned_no_duplicates[
    geolocation_cleaned_no_duplicates[
        "geolocation_zip_code_prefix"
    ] == "38400"
]

print("Total Records:")
print(len(zip_38400_cleaned))

print("\nUnique Coordinate Combinations:")
print(
    zip_38400_cleaned[
        ["geolocation_lat", "geolocation_lng"]
    ].drop_duplicates().shape[0]
)

print("\nUnique City Names:")
print(zip_38400_cleaned["geolocation_city"].unique())
#finding how many postal codes have multiple city names in our duplicate-free dataset.
cities_per_zip_cleaned = (
    geolocation_cleaned_no_duplicates
    .groupby("geolocation_zip_code_prefix")[
        "geolocation_city"
    ].nunique()
)

print("Postal Codes with Multiple City Names:")
print((cities_per_zip_cleaned > 1).sum())

print("\nMaximum City Names for One Postal Code:")
print(cities_per_zip_cleaned.max())
#identify the postal code with maximum citiees
print("Postal Code with Maximum City Names:")
print(cities_per_zip_cleaned.idxmax())

print("\nMaximum Number of City Names:")
print(cities_per_zip_cleaned.max())
#inspect postal code 06900
zip_06900 = geolocation_cleaned_no_duplicates[
    geolocation_cleaned_no_duplicates[
        "geolocation_zip_code_prefix"
    ] == "06900"
]

print("Unique City Names:")
print(zip_06900["geolocation_city"].unique())

print("\nCity Name Counts:")
print(zip_06900["geolocation_city"].value_counts())

print("\nAssociated States:")
print(zip_06900["geolocation_state"].unique())
#check cleaned dataset contains any missing sates and city values
print("Missing Values:")
print(geolocation_cleaned_no_duplicates[
    ["geolocation_city", "geolocation_state"]
].isnull().sum())
#checking invalid coordinates after removing duplicates
invalid_coordinates_cleaned = geolocation_cleaned_no_duplicates[
    (geolocation_cleaned_no_duplicates["geolocation_lat"] < -34) |
    (geolocation_cleaned_no_duplicates["geolocation_lat"] > 6) |
    (geolocation_cleaned_no_duplicates["geolocation_lng"] < -74) |
    (geolocation_cleaned_no_duplicates["geolocation_lng"] > -34)
]

print("Unusual Coordinate Records:")
print(len(invalid_coordinates_cleaned))
#detail of unsual coordinates
print("Unusual Coordinate Records:")
print(
    invalid_coordinates_cleaned[
        [
            "geolocation_zip_code_prefix",
            "geolocation_lat",
            "geolocation_lng",
            "geolocation_city",
            "geolocation_state"
        ]
    ].sort_values("geolocation_zip_code_prefix")
)
#verify the filter coordinate
print("Records violating latitude range:")
print(
    (
        (geolocation_cleaned_no_duplicates["geolocation_lat"] < -34) |
        (geolocation_cleaned_no_duplicates["geolocation_lat"] > 6)
    ).sum()
)

print("\nRecords violating longitude range:")
print(
    (
        (geolocation_cleaned_no_duplicates["geolocation_lng"] < -74) |
        (geolocation_cleaned_no_duplicates["geolocation_lng"] > -34)
    ).sum()
)

print("\nRecords violating either range:")
print(len(invalid_coordinates_cleaned))
#investigate the 33 records by state
print("Unusual Coordinate Records by State:")
print(
    invalid_coordinates_cleaned["geolocation_state"]
    .value_counts()
)
#final cleaned dataset
geolocation_cleaned_final = geolocation_cleaned_no_duplicates.copy()

geolocation_cleaned_final["coordinate_flag"] = np.where(
    (geolocation_cleaned_final["geolocation_lat"] < -34) |
    (geolocation_cleaned_final["geolocation_lat"] > 6) |
    (geolocation_cleaned_final["geolocation_lng"] < -74) |
    (geolocation_cleaned_final["geolocation_lng"] > -34),
    "Review",
    "Within Approximate Range"
)

print("Final Dataset Shape:")
print(geolocation_cleaned_final.shape)

print("\nCoordinate Flag Counts:")
print(geolocation_cleaned_final["coordinate_flag"].value_counts())
#verify our final dataset
print("Final Dataset Shape:")
print(geolocation_cleaned_final.shape)

print("\nDuplicate Rows:")
print(geolocation_cleaned_final.duplicated().sum())

print("\nPostal Code Lengths:")
print(geolocation_cleaned_final[
    "geolocation_zip_code_prefix"
].str.len().value_counts())

print("\nMissing Values:")
print(geolocation_cleaned_final.isnull().sum())
#save the clean geolocation dataset
geolocation_cleaned_final.to_csv(
    "Data/cleaned/geolocation_cleaned.csv",
    index=False
)

print("Cleaned Geolocation Dataset Saved Successfully!")
#verifying the saved csv
geolocation_check = pd.read_csv(
    "Data/cleaned/geolocation_cleaned.csv",
    dtype={"geolocation_zip_code_prefix": str}
)

print("Saved Dataset Shape:")
print(geolocation_check.shape)

print("\nFirst 5 Records:")
print(geolocation_check.head())

print("\nPostal Code Data Type:")
print(geolocation_check["geolocation_zip_code_prefix"].dtype)