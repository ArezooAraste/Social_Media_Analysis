# =====================================================
# Social Media Content Performance Analytics
# Data Cleaning & Feature Engineering Pipeline
# =====================================================


# ==========================
# 1. Import Libraries
# ==========================

import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler


# ==========================
# 2. Load Raw Dataset
# ==========================

file_path = "Social Media Content Performance Dataset.xlsx"

df = pd.read_excel(file_path)


print("==============================")
print("RAW DATA OVERVIEW")
print("==============================")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.info())


# ==========================
# 3. Data Quality Check
# ==========================

print("\n==============================")
print("MISSING VALUES")
print("==============================")

print(df.isnull().sum())


print("\n==============================")
print("DUPLICATE ROWS")
print("==============================")

print(
    "Duplicate count:",
    df.duplicated().sum()
)


print("\n==============================")
print("UNIQUE VALUES")
print("==============================")

for col in df.columns:
    print(
        col,
        ":",
        df[col].nunique()
    )


# ==========================
# 4. Data Cleaning
# ==========================

df_clean = df.copy()


# Remove duplicates

df_clean = df_clean.drop_duplicates()


# Fix Date Column

df_clean["Post_Published_At"] = pd.to_datetime(
    df_clean["Post_Published_At"],
    errors="coerce"
)


# Remove invalid dates

df_clean = df_clean[
    df_clean["Post_Published_At"].notna()
]


# ==========================
# 5. Create Date Features
# ==========================


df_clean["Post_Date"] = (
    df_clean["Post_Published_At"]
    .dt.date
)


df_clean["Post_Hour"] = (
    df_clean["Post_Published_At"]
    .dt.hour
)


df_clean["Day_Name"] = (
    df_clean["Post_Published_At"]
    .dt.day_name()
)



# ==========================
# 6. Handle Missing Values
# ==========================


# CTR missing values

avg_ctr = (
    df_clean["Click_Through_Rate"]
    .mean()
)


df_clean["CTR_Filled"] = (
    df_clean["Click_Through_Rate"]
    .fillna(avg_ctr)
)



# ==========================
# 7. Feature Engineering
# ==========================


# Share Rate

df_clean["Share_Rate"] = (
    df_clean["Shares"]
    /
    df_clean["Views"]
)


# Comment Rate

df_clean["Comment_Rate"] = (
    df_clean["Comments"]
    /
    df_clean["Views"]
)


# View Efficiency

df_clean["View_Efficiency"] = (
    df_clean["Views"]
    /
    df_clean["Impressions"]
)


# Replace infinity values

df_clean.replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True
)


df_clean.fillna(
    0,
    inplace=True
)



# ==========================
# 8. Performance Score
# ==========================


score_columns = [
    "Engagement_Rate",
    "CTR_Filled",
    "Share_Rate",
    "Comment_Rate",
    "View_Efficiency"
]


scaler = MinMaxScaler()


df_clean[score_columns] = (
    scaler.fit_transform(
        df_clean[score_columns]
    )
)



df_clean["Performance_Score"] = (

    df_clean["Engagement_Rate"] * 0.35

    +

    df_clean["CTR_Filled"] * 0.25

    +

    df_clean["Share_Rate"] * 0.20

    +

    df_clean["Comment_Rate"] * 0.10

    +

    df_clean["View_Efficiency"] * 0.10

)



# ==========================
# 9. Save Clean Dataset
# ==========================


df_clean.to_csv(
    "clean_social_media_data.csv",
    index=False,
    encoding="utf-8-sig"
)


print("\n==============================")
print("CLEANING COMPLETED")
print("==============================")

print(
    "Clean Dataset Shape:",
    df_clean.shape
)

print(
    "File Saved: clean_social_media_data.csv"
)


# =====================================================
# Step 2: Create Dimension Tables
# =====================================================


# ==========================
# 1. Dimension Platform
# ==========================


dim_platform = (
    df_clean[["Platform"]]
    .drop_duplicates()
    .reset_index(drop=True)
)


# Create Primary Key

dim_platform.insert(
    0,
    "Platform_ID",
    range(1, len(dim_platform)+1)
)


print("\nDim Platform:")
print(dim_platform)



# ==========================
# 2. Dimension Content
# ==========================


dim_content = (
    df_clean[
        [
            "Content_Category",
            "Content_Type",
            "Post_Type"
        ]
    ]
    .drop_duplicates()
    .reset_index(drop=True)
)


# Create Primary Key

dim_content.insert(
    0,
    "Content_ID",
    range(1, len(dim_content)+1)
)


print("\nDim Content:")
print(dim_content)



# ==========================
# 3. Dimension Hashtag
# ==========================


dim_hashtag = (
    df_clean[["Main_Hashtag"]]
    .drop_duplicates()
    .reset_index(drop=True)
)


# Create Primary Key

dim_hashtag.insert(
    0,
    "Hashtag_ID",
    range(1, len(dim_hashtag)+1)
)


print("\nDim Hashtag:")
print(dim_hashtag)



# ==========================
# 4. Dimension Date
# ==========================


dim_date = (
    df_clean[["Post_Date"]]
    .drop_duplicates()
    .reset_index(drop=True)
)


# Rename Date Column

dim_date.rename(
    columns={
        "Post_Date": "Date"
    },
    inplace=True
)



# Create Date ID

dim_date.insert(
    0,
    "Date_ID",
    range(1, len(dim_date)+1)
)



# Date Attributes

dim_date["Year"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.year
)


dim_date["Quarter"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.quarter
)


dim_date["Month"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.month
)


dim_date["Month_Name"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.month_name()
)


dim_date["Year_Month"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.strftime("%Y-%m")
)


dim_date["Day_Name"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.day_name()
)


dim_date["Week_Number"] = (
    pd.to_datetime(dim_date["Date"])
    .dt.isocalendar()
    .week
)



print("\nDim Date:")
print(dim_date.head())



# ==========================
# Save Dimensions
# ==========================


dim_platform.to_csv(
    "Dim_Platform.csv",
    index=False,
    encoding="utf-8-sig"
)


dim_content.to_csv(
    "Dim_Content.csv",
    index=False,
    encoding="utf-8-sig"
)


dim_hashtag.to_csv(
    "Dim_Hashtag.csv",
    index=False,
    encoding="utf-8-sig"
)


dim_date.to_csv(
    "Dim_Date.csv",
    index=False,
    encoding="utf-8-sig"
)



print("\n==============================")
print("DIMENSIONS CREATED SUCCESSFULLY")
print("==============================")

# =====================================================
# Step 3: Create Fact Table
# =====================================================


# ==========================
# 1. Create Mapping Tables
# ==========================


# Platform Mapping

platform_map = dict(
    zip(
        dim_platform["Platform"],
        dim_platform["Platform_ID"]
    )
)



# Content Mapping

content_map = (
    dim_content
    .set_index(
        [
            "Content_Category",
            "Content_Type",
            "Post_Type"
        ]
    )["Content_ID"]
    .to_dict()
)



# Hashtag Mapping

hashtag_map = dict(
    zip(
        dim_hashtag["Main_Hashtag"],
        dim_hashtag["Hashtag_ID"]
    )
)



# Date Mapping

date_map = dict(
    zip(
        dim_date["Date"],
        dim_date["Date_ID"]
    )
)



# ==========================
# 2. Add Foreign Keys
# ==========================


df_fact = df_clean.copy()



# Platform ID

df_fact["Platform_ID"] = (
    df_fact["Platform"]
    .map(platform_map)
)



# Content ID

df_fact["Content_ID"] = (
    df_fact[
        [
            "Content_Category",
            "Content_Type",
            "Post_Type"
        ]
    ]
    .apply(tuple, axis=1)
    .map(content_map)
)



# Hashtag ID

df_fact["Hashtag_ID"] = (
    df_fact["Main_Hashtag"]
    .map(hashtag_map)
)



# Date ID

df_fact["Date_ID"] = (
    df_fact["Post_Date"]
    .map(date_map)
)



# ==========================
# 3. Select Fact Columns
# ==========================


fact_post = df_fact[

    [

        # Keys

        "Post_ID",

        "Platform_ID",

        "Content_ID",

        "Hashtag_ID",

        "Date_ID",



        # Metrics

        "Views",

        "Impressions",

        "Engagement",

        "Likes",

        "Shares",

        "Comments",

        "Clicks",

        "Click_Through_Rate",

        "Engagement_Rate",


        # Analytical Features

        "Post_Hour",

        "Performance_Score"

    ]

].copy()



# ==========================
# 4. Check Fact Quality
# ==========================


print("\n==============================")
print("FACT TABLE CHECK")
print("==============================")


print(
    fact_post.head()
)


print("\nMissing Foreign Keys:")


print(
    fact_post[
        [
            "Platform_ID",
            "Content_ID",
            "Hashtag_ID",
            "Date_ID"
        ]
    ]
    .isnull()
    .sum()
)



# ==========================
# 5. Save Fact
# ==========================


fact_post.to_csv(
    "Fact_Post_Performance.csv",
    index=False,
    encoding="utf-8-sig"
)



print("\n==============================")
print("FACT TABLE CREATED SUCCESSFULLY")
print("==============================")