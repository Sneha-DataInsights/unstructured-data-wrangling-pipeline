#!/usr/bin/env python
# coding: utf-8

# ### PROJECT : Unstructured Text Data Cleaning

# In[4]:


#import require library
import pandas as pd


# In[5]:


#1. Load Row Data
df=pd.read_csv(r"C:\Users\Sneha\Downloads\houses.txt",on_bad_lines="skip",header=None,skiprows=[0,1,2])
df.head(20)


# ### Extract header section

# In[6]:


# Extract column names (header section)
header_row=df.iloc[3:17]
header_row


# In[8]:


header=header_row[0].str.split(" ",expand=True)[1]
header


# In[9]:


#Extract actual data (after header)
data=df.iloc[17:]
data


# ### Handle Multiple Line Records using iloc (Each Record =2 rows)

# In[11]:


data_row1=data.iloc[:1028:2]
data_row1


# In[12]:


data_1=data_row1[0].str.split("  ",expand=True)# Split Columns using Multiple Spaces
data_1.reset_index(inplace=True)
data_1


# In[13]:


data_1.drop(columns="index",inplace=True)


# In[14]:


data_1


# In[15]:


data


# In[15]:


#Same Process For Data Row 2
data_row2=data.iloc[1:1029:2]
data_row2


# In[16]:


data_2=data_row2[0].str.split("  ",expand=True)
data_2


# In[17]:


data_2.drop(columns=[0,4],inplace=True)#drop unwanted columns
data_2


# In[18]:


data_2.reset_index(inplace=True)


# In[19]:


data_2.drop(columns="index",inplace=True)
data_2


# # Combine Both Parts to Form complete Records

# In[21]:


finaldata=data_1.join(data_2,rsuffix="data2") #use resuffix for avoiding data overlaping
finaldata.shape


# # assign Column Names 

# In[24]:


header.shape #hence columns count match 


# In[25]:


finaldata.columns=header


# # Final Data Check

# In[26]:


finaldata


# # Save Cleaned data

# In[27]:


finaldata.to_csv(r"C:\Users\Sneha\Desktop\Project_folder\cleaned_housing_data.csv", index=False)

