#                                                                                          EDA ON SALES DATASET

#### Online Sales Analysis  This project analyzes an online sales dataset using Pandas for data cleaning and manipulation, and visualizes insights with Matplotlib, Plotly, and Seaborn. It includes techniques like grouping, pivot tables, and data visualization to reveal key sales trends and patterns.

## Data Collection and Exploration
Description: This section involves loading the dataset and getting an initial understanding of the data.

Tasks:
1.Load the dataset using Pandas.
2.Display the first few rows.
3.Check for null values and data types.
4.Get descriptive statistics of the dataset.

## Data Preprocessing
Description: Prepare the data for analysis by cleaning and transforming it.

Tasks:
1.Handling Missing Values: Remove or fill missing data.
2.Data Type Conversion: Convert data types (e.g., dates to datetime).
3.Feature Extraction: Extract additional features like month, hour, etc., from the order date.
4.Handling Duplicates: Remove duplicate entries if any.
5.Address Parsing: Separate the purchase address into city, state, and zip code.

## Exploratory Data Analysis (EDA) and Visualization
Description: Perform analysis and create visualizations to uncover insights.

Tasks:
1.Monthly Sales Analysis: Analyze sales trends over different months to identify seasonal patterns and peak sales periods.
2.State-wise Sales Analysis: Analyze sales distribution across different states to understand regional performance at a state level.
3.City-wise Sales Analysis: Analyze sales distribution across different cities to understand regional performance and identify high-performing areas.
4.Peak Time Analysis: Identify peak order times to optimize staffing,inventory management and Advertisement.
5.Products Sold Together: Analyze which products are frequently bought together to identify bundling opportunities and cross-selling strategies
6.Product Sales Analysis: Determine the most and least sold products to identify bestsellers and underperformers.
6.1:Correlation Analysis: Explore the relationship between quantity ordered and price to understand pricing strategies and their impact on sales.


#                                                                                INSIGHTS

      
### 1.	Monthly Sales Analysis: 

Key Insights:
A.	Seasonal Trends: There are noticeable peaks and dips in sales throughout the year. For example, sales peak significantly in March and November, indicating these months might have higher demand or successful promotional campaigns.
B.	Low Sales Periods: April shows a sharp decline in sales following the March peak. This could indicate a post-peak slump or seasonal variation.
C.	Consistent Performance: Some months, like May and June, show relatively stable sales without significant fluctuations.
D.	Highest Sales: November has the highest sales on the graph, suggesting it might be a crucial month for business, possibly due to holiday shopping or special events.

### 2.	State-wise Sales Analysis

A.	
•	California (CA): Dominates the sales distribution with 39.8% of total sales, indicating a significant market presence and customer base in this state.
•	New York (NY): Accounts for 13.5% of sales, making it the second-highest contributor.
•	Texas (TX): Close behind NY with 13.3% of sales, showing strong performance in this state as well.
•	Georgia (GA): Contributes 10.6% to the sales, indicating a notable market share.
•	Massachusetts (MA): Holds 7.9% of the sales distribution.
•	Virginia (VA): Accounts for 6.1% of sales.
•	Oregon (OR): Represents 5.4% of the sales.
•	Maine (ME): Has the smallest share among the listed states with 3.4% of sales.

B.	Key Insights:
•	California is the leading state in terms of sales, suggesting it is a key market for the business.
•	New York and Texas also have substantial sales, indicating strong market performance in these states.

### 3.	City-wise Sales Analysis

A.	Best City Sales-Wise:
•	San Francisco leads with the highest sales, reaching close to $1 million.
•	Other cities like New York City, Los Angeles, Dallas, Portland, and Austin follow, but with significantly lower sales.

B.	Best City Quantity-Wise:

•	San Francisco also tops in terms of quantity sold, with just below 50,000 units.
•	Similar to the sales graph, other cities like New York City, Los Angeles, Dallas, Portland, and Austin have lower quantities sold.

•	Key Insights:
•	San Francisco is the top-performing city both in terms of sales revenue and quantity sold, indicating a strong market presence and customer base.
•	The consistency in San Francisco’s performance across both metrics suggests effective marketing strategies, high demand, or a combination of both.
•	Other cities, while performing well, have room for growth compared to San Francisco.
•	
### 4.	Peak Time Analysis:

1.	Peak Sales Hours: There are significant peaks around 11 AM and 8 PM, indicating these are the times when the highest number of products are sold. This could be due to increased online activity during these hours.
2.	Low Sales Hours: Sales are notably low around 4 AM and 4 PM, suggesting these times have the least customer activity.
3.	Consistent Sales: Between 6 AM and 10 AM, sales gradually increase, showing a steady rise in customer purchases during the morning hours.
4.	Evening Surge: After a dip in the afternoon, there is a noticeable surge in sales starting from 6 PM, peaking at 8 PM.
   
Key Insights:
•	Morning and Evening Peaks: The business experiences the highest sales during late morning and evening hours, which could be targeted for promotions and marketing campaigns.
•	Low Activity Periods: Early morning and mid-afternoon show the lowest sales, which might be ideal times for system maintenance or inventory updates.

### 5.	Products Sold Together:
        
1.	Most Frequent Combination: The combination of iPhone and Lightning Charging Cable is the most frequent, with a frequency close to 1000. This indicates a high demand for this pairing, possibly due to the popularity of iPhones and the necessity of charging accessories.
2.	Other Popular Combinations:
o	Google Phone and USB-C Charging Cable: This combination also shows a high frequency, suggesting a strong demand for Google phones and their charging accessories.
o	iPhone and Wired Headphones: Another popular combination, indicating that many iPhone users also purchase wired headphones.
3.	Less Frequent Combinations: Combinations like Vareebadd Phone and Wired Headphones and Lightning Charging Cable and Wired Headphones have lower frequencies, indicating less demand for these pairings.
Key Insights:
•	Accessory Demand: Charging cables and headphones are frequently purchased with phones, highlighting the importance of these accessories.
•	Brand Popularity: iPhone-related combinations dominate the graph, suggesting a strong market presence for Apple products.
•	Cross-Selling Opportunities: Identifying popular product combinations can help in creating effective bundling and cross-selling strategies.

### 6.	Product Sales Analysis and Correlation Analysis:

1.	  High Sales Volume:
o	AA Batteries (4-pack) and AAA Batteries (4-pack) have the highest sales volumes, indicating these are popular, frequently purchased items.
o	Lightning Charging Cable and USB-C Charging Cable also show high sales, reflecting the demand for phone accessories.
2.	Low Sales Volume:
o	Products like LG Washing Machine and LG Dryer have much lower sales volumes, suggesting these high-priced items are less frequently purchased.
3.	Price vs. Quantity:
o	There is an inverse relationship between price and quantity sold. Cheaper items like batteries and charging cables sell in higher quantities, while more expensive items like monitors and laptops sell in lower quantities.
o	The line graph shows that products with higher average prices, such as Macbook Pro Laptop and ThinkPad Laptop, have lower sales volumes.

Key Insights:
•	Accessory Demand: Phone accessories and batteries are top sellers, indicating a strong market for these items.
•	High-Value Items: Expensive products have lower sales volumes, which could be due to their higher price points.
•	Sales Strategy: Understanding the relationship between price and sales volume can help in pricing strategies and inventory management.

