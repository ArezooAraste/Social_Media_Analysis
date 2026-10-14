# 📊 Social Media Content Performance Analytics

## Project Overview

This project is an end-to-end **Social Media Content Performance
Analytics** solution designed to analyze content performance across
multiple platforms and identify the factors that drive engagement.

The project workflow:

**Data Cleaning → Feature Engineering → Data Modeling → DAX Analytics →
Power BI Dashboard**

The goal is to transform raw social media data into actionable insights
for marketing and content strategy decisions.

------------------------------------------------------------------------

# 🎯 Business Objectives

This project answers key marketing analytics questions:

-   Which platforms generate stronger engagement?
-   Which content categories and content types perform best?
-   Which content strategies should be prioritized?
-   How does publishing time affect engagement?
-   How can performance metrics be used to compare content quality?

------------------------------------------------------------------------

# 🛠️ Tools & Technologies

  Tool           Purpose
  -------------- -------------------------------------
  Python         Data Cleaning & Feature Engineering
  Pandas         Data Transformation
  NumPy          Data Processing
  Scikit-learn   Feature Scaling
  Power BI       Dashboard Development
  DAX            Analytical Measures
  Star Schema    Data Modeling

------------------------------------------------------------------------

# 🔄 Data Preparation Pipeline

The data preparation process was implemented using Python.

The pipeline includes:

-   Loading raw dataset
-   Data quality checks
-   Missing value analysis
-   Duplicate detection
-   Data cleaning
-   Feature engineering
-   Creating dimension tables
-   Creating fact table

Workflow:

    Raw Dataset
          ↓
    Python Data Cleaning Pipeline
          ↓
    Clean Analytical Tables
          ↓
    Power BI Data Model
          ↓
    Interactive Dashboard

------------------------------------------------------------------------

# 🧹 Data Cleaning & Feature Engineering

Cleaning steps:

-   Removed duplicate records
-   Converted publication timestamps into datetime format
-   Removed invalid dates
-   Handled missing CTR values
-   Replaced invalid numeric values

Created analytical features:

-   Share Rate
-   Comment Rate
-   View Efficiency
-   Post Hour
-   Day Name

------------------------------------------------------------------------

# 📊 Performance Score

A composite Performance Score was created to evaluate content quality.

The score combines:

-   Engagement Rate (35%)
-   CTR (25%)
-   Share Rate (20%)
-   Comment Rate (10%)
-   View Efficiency (10%)

The score allows comparison between different content strategies beyond
simple engagement volume.

------------------------------------------------------------------------

# 🏗️ Data Modeling

The project uses a Star Schema architecture.

                     Dim_Date

                        |

    Dim_Platform — Fact_Post_Performance — Dim_Content

                        |

                  Dim_Hashtag

## Fact Table

### Fact_Post_Performance

Contains:

-   Post_ID
-   Platform_ID
-   Content_ID
-   Hashtag_ID
-   Date_ID
-   Views
-   Impressions
-   Engagement
-   Likes
-   Shares
-   Comments
-   Clicks
-   Click Through Rate
-   Engagement Rate
-   Post Hour
-   Performance Score

------------------------------------------------------------------------

## Dimension Tables

### Dim_Platform

Contains platform information.

### Dim_Content

Contains:

-   Content Category
-   Content Type
-   Post Type

### Dim_Hashtag

Contains hashtag information for hashtag performance analysis.

### Dim_Date

Contains:

-   Date
-   Year
-   Quarter
-   Month
-   Month Name
-   Year Month
-   Day Name
-   Week Number

------------------------------------------------------------------------

# 📐 DAX Measures

The Power BI model contains focused analytical measures:

## Performance Metrics

-   Avg Engagement per Post
-   Avg Engagement Rate
-   Avg Performance Score
-   Avg Views per Post
-   Best Performance Score

## Engagement Metrics

-   Total Engagement
-   Total Likes
-   Total Shares
-   Engagement Contribution

## Volume Metrics

-   Total Posts
-   Total Views
-   Post Count

------------------------------------------------------------------------

# 📈 Dashboard Analysis

## Page 1 --- Marketing Performance Overview

Includes:

-   KPI Overview
-   Platform Engagement Analysis
-   Content Category Performance
-   Top Performing Content Strategies
-   Engagement Contribution Analysis

Main KPIs:

-   Total Posts: 5,600
-   Total Views: 5bn
-   Total Engagement: 646M
-   Avg Engagement Rate: 46.88%
-   Avg Performance Score: 0.47

------------------------------------------------------------------------

## Page 2 --- Content Strategy Analysis

Includes:

-   Content Opportunity Matrix
-   Platform & Content Performance Matrix
-   Top Performing Strategies Ranking

Focus areas:

-   Platform performance
-   Content category comparison
-   Content type evaluation
-   Performance Score analysis

------------------------------------------------------------------------

## Page 3 --- Timing & Audience Insights

Includes:

-   Best Posting Time Analysis
-   Engagement Trend by Posting Time
-   Day Type Analysis
-   Hashtag Performance Analysis

------------------------------------------------------------------------

# 🔍 Key Insights

Key findings from the analysis:

-   Content performance differs significantly across platforms and
    content categories.
-   Educational and Customer Story content categories demonstrate strong
    performance.
-   Performance Score provides a balanced evaluation by combining
    multiple engagement indicators.
-   Posting time analysis helps identify stronger publishing windows.
-   Hashtag analysis provides additional context for content
    optimization.

------------------------------------------------------------------------

# 📂 Repository Structure

    Social-Media-Analytics/

    │
    ├── Data/
    │   ├── clean_social_media_data.csv
    │   ├── Dim_Content.csv
    │   ├── Dim_Date.csv
    │   ├── Dim_Hashtag.csv
    │   ├── Dim_Platform.csv
    │   └── Fact_Post_Performance.csv
    │
    ├── Python/
    │   └── social_media_analysis.py
    │
    ├── PowerBI/
    │   └── dashboard.pbix
    │
    ├── Screenshots/
    │   ├── dashboard_overview.png
    │   ├── content_strategy.png
    │   ├── timing_insights.png
    │
    └── README.md

Dashboard screenshots are available inside the **Screenshots** folder.

------------------------------------------------------------------------

# 🚀 Future Improvements

Potential improvements:

-   Sentiment analysis from comments
-   Predictive engagement modeling
-   Automated dashboard refresh
-   Machine learning based content recommendations
-   NLP-based hashtag optimization

------------------------------------------------------------------------

# 👤 Author

## **Arezoo Araste**

**B2B Data Analyst \| Sales Funnel & Marketing Analytics \| Power BI
Developer**

🔗 LinkedIn: https://www.linkedin.com/in/arezoo-araste/

💻 GitHub: https://github.com/ArezooAraste

📧 Email: arezooaraste7@gmail.com
