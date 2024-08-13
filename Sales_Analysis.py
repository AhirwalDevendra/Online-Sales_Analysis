#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# ### Data Collection and Exploration

# Description: This section involves loading the dataset and getting an initial understanding of the data.
#     
# Tasks:
#     
# 1.Load the dataset using Pandas.
# 
# 2.Display the first few rows.
# 
# 3.Check for null values and data types.
# 
# 4.Get descriptive statistics of the dataset.

# In[2]:


files=[file for file in os.listdir(r'C:\Users\DEVEN\Desktop\FINALE\PYTHONN\PROJECT\MONTHLY SALES')]


# In[3]:


files


# In[4]:


data=pd.DataFrame()


# In[5]:


for file in files:
    df1=pd.read_csv("C:/Users/DEVEN/Desktop/FINALE/PYTHONN/PROJECT/MONTHLY SALES/" +file)
    data=pd.concat([data,df1],ignore_index=True)


# In[6]:


data


# In[7]:


data .isna().sum()


# In[8]:


data=data.dropna()  # dropped nulls


# In[9]:


data.info()  # all are object type


# In[10]:


data.duplicated().sum()


# In[11]:


data.shape


# In[12]:


data.head(2)


# ### Data Preprocessing

# Description: Prepare the data for analysis by cleaning and transforming it.
# 
# Tasks:
# 
#    1.Handling Missing Values: Remove or fill missing data.
#    
#    2.Data Type Conversion: Convert data types (e.g., dates to datetime).
#    
#    3.Feature Extraction: Extract additional features like month, hour, etc., from the order date.
# 
#    4.Handling Duplicates: Remove duplicate entries if any.
# 
#    5.Address Parsing: Separate the purchase address into city, state, and zip code.
#                         

# In[13]:


data.columns


# In[14]:


import warnings
warnings.filterwarnings('ignore')


# In[15]:


data['Quantity Ordered']=pd.to_numeric(data['Quantity Ordered'],errors='coerce')
data['Price Each']=pd.to_numeric(data['Price Each'],errors='coerce')
data['Sales']=(data['Quantity Ordered'])*(data['Price Each'])


# In[16]:


data.head(2)


# In[17]:


data[['City','Zip']]=data['Purchase Address'].str.split(',',expand=True).iloc[:,1:]
data['State']=data['Zip'].str[1:3]
data['Zip']=data['Zip'].str[3:]


# In[18]:


data.head(2)


# In[19]:


data['Order Date']=pd.to_datetime(data['Order Date'],errors='coerce')
data['Month']=pd.to_datetime(data['Order Date'],errors='coerce').dt.month
data['Hour']=pd.to_datetime(data['Order Date'],errors='coerce').dt.hour


# In[20]:


data.head(2)


# In[21]:


data.info()


# In[22]:


data.describe()


# In[23]:


data.shape


# In[24]:


data.isna().sum()


# In[25]:


data.duplicated().sum()


# In[26]:


data[data['Order ID']=='176585']


# In[27]:


data=data.dropna()  # It will dropp NaN,Nat,None
data=data.drop_duplicates()
#data=data.drop(columns='Purchase Address')


# In[28]:


data.head()


# In[29]:


data.shape


# In[30]:


data.info()


# In[31]:


data=data[data['Order Date'].dt.year==2019]  #very few data for 2020 ,hence kept data for only 2019
data=data.reset_index(drop=True)


# In[32]:


data.head()


# In[33]:


data.to_csv(r'C:\Users\DEVEN\Desktop\FINALE\PYTHONN\PROJECT\Final Submission\Cleaned_Sales_Dataset.csv')


# # Exploratory Data Analysis (EDA) and Visualization

# Description: Perform analysis and create visualizations to uncover insights.
# 
# Tasks:
# 
# 1.Monthly Sales Analysis:  Analyze sales trends over different months to identify seasonal patterns and peak sales periods.
#     
# 2.State-wise Sales Analysis:  Analyze sales distribution across different states to understand regional performance at a state level.
# 
# 
#         
# 3.City-wise Sales Analysis:  Analyze sales distribution across different cities to understand regional performance and identify high-performing areas.
# 
# 4.Peak Time Analysis:  Identify peak order times to optimize staffing,inventory management and Advertisement.
#   
# 
# 5.Products Sold Together:  Analyze which products are frequently bought together to identify bundling opportunities and cross-selling strategies
#         
# 6.Product Sales Analysis:  Determine the most and least sold products to identify bestsellers and underperformers.
# 
# 6.1Correlation Analysis:  Explore the relationship between quantity ordered and price to understand pricing strategies and their impact on sales.
# 

# ### Question 1: What was the best month for sales? How much was earned that month?

# In[34]:


Monthly_Sales=data.groupby('Month')['Sales'].sum().reset_index()
Monthly_Sales['Month']=pd.to_datetime(Monthly_Sales['Month'], format='%m').dt.strftime('%B')


# In[35]:


data.groupby('Month')['Sales'].sum().reset_index()


# In[36]:


plt.plot(Monthly_Sales['Month'],Monthly_Sales['Sales'],marker='v',linewidth=2,color='g')
plt.xlabel('Months',color='g')
plt.ylabel('Sales in Million($)')
plt.title('Monthly Sales')
plt.xticks(rotation=45)

plt.show()

December was the Best Month For Sale
Sales=4608295.70 $
# ### Question 2 Identify state with the highest sales to draw attention to its significant contribution.
# 

# In[37]:


State=data.groupby('State')['Sales'].sum().reset_index()


# In[38]:


fig=px.pie(State, names='State', values='Sales', title='Sales Distribution by State', color='State')
fig.show()

California contributed the most in the Sales,
Sales= 13703047.83 $
# ### Question 3: Which city sold the most product?

# In[39]:


city=data.groupby('City')['Sales'].sum().reset_index().sort_values(by='Sales',ascending=False)
Qnty=data.groupby('City')['Quantity Ordered'].sum().reset_index().sort_values(by='Quantity Ordered',ascending=False)


# In[40]:


plt.figure(figsize=(10,4))

plt.subplot(1,2,1)                           # made subplot one row two column and assign this plot at 1st position

plt.bar(city['City'],city['Sales'],color='r')
plt.xlabel('Cities')
plt.ylabel('Sales in Million($)')
plt.title('Best City Sales-Wise')
plt.xticks(rotation=90)


plt.subplot(1,2,2)   

# assign this plot at 1st position
plt.bar(Qnty['City'],Qnty['Quantity Ordered'],color='g')
plt.xlabel('Cities')
plt.ylabel('Quantity')
plt.title('Best City Quantity-Wise')
plt.xticks(rotation=90)

plt.subplots_adjust(wspace=0.5) # space between two subplots

plt.show()

San Francisco Sold The most Product
# ### Question 4 : At what time should we display advertisements to maximize the likelihood of a customer buying a product?

# In[41]:


Advertise=data.pivot_table(index='Hour',values='Product',aggfunc='count').reset_index()
x=np.arange(0,24)


# In[42]:


plt.figure(figsize=(7.5, 4))
sns.lineplot(x='Hour', y='Product', data=Advertise, marker='o', color='#363c54')

plt.xticks(np.arange(0, 24))
plt.title("Product Sales by Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Products Sold")

plt.show()

From 10AM till 9PM is the best time to display advertisements
# ### Question 5: What products are most often sold together?

# In[43]:


df =data[data['Order ID'].duplicated(keep=False)] # Filter the DataFrame 'df' to get only the rows where 'Order ID' is duplicated

df['Combos'] = df.groupby('Order ID')['Product'].transform(lambda x:','.join(x)) 
                # Create a new column 'Combos' in 'df'
                # Group the filtered DataFrame by 'Order ID' and then use the transform function
                # The lambda function joins all products for the same 'Order ID' into a single string, separated by commas.

df=df[['Order ID','Combos']].drop_duplicates()
                # Keep only the 'Order ID' and 'Combos' columns, and remove any duplicate rows
df.head(2)


# In[44]:


from collections import Counter
from itertools import combinations


# In[45]:


cnt = Counter()            # an empty Counter to count product pairs.     

for row in df['Combos']:    # Go through each row in the 'Combos' column.  
    row_list = row.split(',')   # Split the row into a list of products.
    cnt.update(Counter(combinations(row_list,2)))     # Find all pairs of products in the list.


# In[46]:


top10_combos=cnt.most_common(10) #extracted top 10 combos
top10_combos    #single list returned


# In[47]:


Top_Combos=pd.DataFrame(top10_combos,columns=['combos','Frequency'])  #created 2 columns and converted into dataframe
Top_Combos


# In[48]:


Top_Combos['combos']=Top_Combos['combos'].apply(lambda x:str(x))

#cobmos column is tupple dtype/object not a string ,conerted into string

Top_Combos['combos']=Top_Combos['combos'].apply(lambda x:x.replace('(','').replace(')', '').replace("'", '')) 

#replaced brackets '(' &')' and ' with blank

Top_Combos_sorted=Top_Combos.sort_values(by='Frequency').reset_index(drop=True) 

#sorted in ascending

Top_Combos_sorted


# In[49]:


plt.figure()
plt.barh(Top_Combos_sorted['combos'],Top_Combos_sorted['Frequency'].sort_values(ascending=True),color='#4dc592')
plt.xlabel('Frequency')
plt.ylabel('Product_Combinations')
plt.show()


# ###  Question 6: Which product sold the most?

# In[50]:


Best_product=data.groupby('Product')['Quantity Ordered'].sum().reset_index()


# In[51]:


plt.barh(Best_product['Product'],Best_product['Quantity Ordered'],color='#374b3e')
plt.xlabel('Quantity')
plt.ylabel('Products')
# p2.set_xticklabels(price['Product'],rotation=90)
plt.xticks(rotation=90)
plt.show()


# ### 6.1 : Why those products sold the most?

# In[52]:


price=data.pivot_table(index='Product',values='Price Each').reset_index()
price


# In[53]:


plt.bar(Best_product['Product'],Best_product['Quantity Ordered'],color='g')
plt.ylabel('Quantity')
plt.xlabel('Products')
plt.xticks(rotation=90)

p2=plt.twinx()
plt.plot(price['Product'],price['Price Each'],color='#374b3e',linewidth=1,marker='d',markersize=4)
p2.set_ylabel('Average Price')

plt.show()

AAA Batteries (4-pack) Sold the Most its price is only 2.99$
Because Lower the Price Higher Sales.