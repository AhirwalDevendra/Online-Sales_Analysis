# EDA on Sales Dataset

## Overview
This project analyzes an online sales dataset using Pandas for data cleaning and manipulation, and visualizes insights with Matplotlib, Plotly, and Seaborn. It includes techniques like grouping, pivot tables, and data visualization to reveal key sales trends and patterns.

## Data Collection and Exploration
**Description**: This section involves loading the dataset and getting an initial understanding of the data.

**Tasks:**
- Load the dataset using Pandas.
- Display the first few rows.
- Check for null values and data types.
- Get descriptive statistics of the dataset.

## Data Preprocessing
**Description**: Prepare the data for analysis by cleaning and transforming it.

**Tasks:**
- **Handling Missing Values**: Remove or fill missing data.
- **Data Type Conversion**: Convert data types (e.g., dates to datetime).
- **Feature Extraction**: Extract additional features like month, hour, etc., from the order date.
- **Handling Duplicates**: Remove duplicate entries if any.
- **Address Parsing**: Separate the purchase address into city, state, and zip code.

## Exploratory Data Analysis (EDA) and Visualization
**Description**: Perform analysis and create visualizations to uncover insights.

**Tasks:**
- **Monthly Sales Analysis**: Analyze sales trends over different months to identify seasonal patterns and peak sales periods.
- **State-wise Sales Analysis**: Analyze sales distribution across different states to understand regional performance at a state level.
- **City-wise Sales Analysis**: Analyze sales distribution across different cities to understand regional performance and identify high-performing areas.
- **Peak Time Analysis**: Identify peak order times to optimize staffing, inventory management, and advertisement.
- **Products Sold Together**: Analyze which products are frequently bought together to identify bundling opportunities and cross-selling strategies.
- **Product Sales Analysis**: Determine the most and least sold products to identify bestsellers and underperformers.
- **Correlation Analysis**: Explore the relationship between quantity ordered and price to understand pricing strategies and their impact on sales.

## Insights

### 1. Monthly Sales Analysis:
**Key Insights**:
- **Seasonal Trends**: Sales peak in March and November, indicating high demand or successful promotional campaigns.
- **Low Sales Periods**: April shows a sharp decline in sales, which could indicate a post-peak slump.
- **Consistent Performance**: Months like May and June show stable sales.
- **Highest Sales**: November has the highest sales, possibly due to holiday shopping.

### 2. State-wise Sales Analysis:
**Key Insights**:
- **California (CA)**: Dominates sales with 39.8% of total sales, suggesting a strong market presence.
- **New York (NY)** and **Texas (TX)**: Significant contributors to sales with 13.5% and 13.3%, respectively.

### 3. City-wise Sales Analysis:
**Key Insights**:
- **San Francisco**: Top-performing city both in terms of sales revenue and quantity sold.
- **Sales Distribution**: Other cities like New York City and Los Angeles follow but with significantly lower sales.

### 4. Peak Time Analysis:
**Key Insights**:
- **Morning and Evening Peaks**: Sales are highest around 11 AM and 8 PM.
- **Low Activity Periods**: Sales are low at 4 AM and 4 PM, indicating periods of low customer activity.

### 5. Products Sold Together:
**Key Insights**:
- **Accessory Demand**: Items like charging cables and headphones are frequently purchased with phones, highlighting the importance of accessories.
- **Cross-Selling Opportunities**: Popular product combinations suggest opportunities for bundling.

### 6. Product Sales Analysis and Correlation Analysis:
**Key Insights**:
- **High Sales Volume**: Items like AA and AAA batteries, as well as charging cables, show high sales volumes.
- **Price vs. Quantity**: There is an inverse relationship between price and quantity sold, where cheaper items sell in higher quantities.
- **Sales Strategy**: Understanding the relationship between price and sales volume can guide inventory and pricing decisions.

## Technologies Used:
- **Python**
- **Pandas**
- **Matplotlib**
- **Plotly**
- **Seaborn**
