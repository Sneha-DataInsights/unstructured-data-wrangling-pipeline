#!/usr/bin/env python
# coding: utf-8

# ### PROJECT : Unstructured Text Data Cleaning

# In[3]:


#import require library
import pandas as pd


# In[14]:


#1. Load Row Data
df=pd.read_csv(r"C:\Users\Sneha\Downloads\houses.txt",on_bad_lines="skip",header=None,skiprows=[0,1,2])
df.head(20)


# ### Extract header section

# In[15]:


# Extract column names (header section)
header_row=df.iloc[3:17]
header_row


# In[16]:


header=header_row[0].str.split(" ",expand=True)[1]
header


# In[17]:


#Extract actual data (after header)
data=df.iloc[17:]
data


# ### Handle Multiple Line Records using iloc (Each Record =2 rows)

# In[18]:


data_row1=data.iloc[:1028:2]
data_row1


# In[19]:


data_1=data_row1[0].str.split("  ",expand=True)# Split Columns using Multiple Spaces
data_1.reset_index(inplace=True)
data_1


# In[20]:


data_1.drop(columns="index",inplace=True)


# In[21]:


data_1.isnull().value_counts()


# In[22]:


data


# In[23]:


#Same Process For Data Row 2
data_row2=data.iloc[1:1029:2]
data_row2


# In[24]:


data_2=data_row2[0].str.split("  ",expand=True)
data_2


# In[25]:


data_2.drop(columns=[0,4],inplace=True)#drop unwanted columns
data_2


# In[26]:


data_2.reset_index(inplace=True)


# In[27]:


data_2.drop(columns="index",inplace=True)
data_2


# # Combine Both Parts to Form complete Records

# In[28]:


finaldata=data_1.join(data_2,rsuffix="data2") #use resuffix for avoiding data overlaping
finaldata.shape


# # assign Column Names 

# In[29]:


header.shape #hence columns count match 


# In[30]:


finaldata.columns=header


# # Final Data Check

# In[31]:


finaldata


# ### Data Validation Check

# In[32]:


finaldata.isnull().sum()


# In[33]:


finaldata.duplicated().sum()


# In[35]:


print("--- Missing Values Per Column ---")
print(finaldata.isnull().sum())
print("\n--- Total Duplicate Rows ---")
print(finaldata.duplicated().sum())
print("\n--- Data Structure Overview ---")
finaldata.info()


# In[36]:


# Convert all columns to numeric, turning any remaining uncleaned text into NaN
finaldata = finaldata.apply(pd.to_numeric, errors='coerce')

# Verify the changes
finaldata.info()


# In[37]:


# Fill the missing values in column 'B' with its median
finaldata['B'] = finaldata['B'].fillna(finaldata['B'].median())

# Verify that there are absolutely no null values left
print(finaldata.isnull().sum())


# # Save Cleaned data

# In[38]:


finaldata.to_csv(r"C:\Users\Sneha\Desktop\unstructured-data-cleaning-project\cleaned_housing_data.csv", index=False)


# ### Exploratory data analysis (EDA)

# In[41]:


# Calculate correlations
correlation_matrix = finaldata.corr()

# Look specifically at what correlates most with home prices (MEDV)
print(correlation_matrix['MEDV'].sort_values(ascending=False))


# In[39]:


import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(finaldata['MEDV'], kde=True)
plt.title('Distribution of Median Home Values')
plt.xlabel('MEDV (in $1000s)')
plt.show()


# In[40]:


sns.scatterplot(x='RM', y='MEDV', data=finaldata)
plt.title('Impact of Number of Rooms on Home Price')
plt.xlabel('Average Number of Rooms (RM)')
plt.ylabel('Median Value (MEDV)')
plt.show()


# In[ ]:




