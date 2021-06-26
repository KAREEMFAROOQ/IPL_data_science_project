#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


ipl=pd.read_csv('F:\Match.csv')
ipl.head()


# In[34]:


ipl


# In[6]:


ipl.shape


# In[7]:


ipl['ManOfMach'].value_counts()


# In[8]:


ipl['ManOfMach'].value_counts()[0:10]


# In[9]:


ipl['ManOfMach'].value_counts()[0:5]


# In[10]:


list(ipl['ManOfMach'].value_counts()[0:5].keys())


# In[11]:


plt.bar(list(ipl['ManOfMach'].value_counts()[0:5].keys()),list(ipl['ManOfMach'].value_counts()[0:5]),color='red')
plt.show()


# In[12]:


ipl['Outcome_Type'].value_counts()


# In[13]:


ipl['Toss_Winner'].value_counts()


# In[14]:


first_batting=ipl[ipl['Win_Type']!='wickets']


# In[15]:


first_batting.head(10)


# In[16]:


plt.figure(figsize=(6,6))
plt.hist(first_batting['Win_Margin'])
plt.xlabel("Runs")
plt.title("Distribution of Runs")
plt.show()


# In[17]:


first_batting['match_winner'].value_counts()


# In[18]:


ipl['match_winner'].value_counts()


# In[19]:


list(ipl['match_winner'].value_counts()[0:5])


# In[20]:


list(ipl['match_winner'].value_counts()[0:5].keys())


# In[21]:


plt.figure(figsize=(10,6))
plt.plot(list(ipl['match_winner'].value_counts()[0:5].keys()),list(ipl['match_winner'].value_counts()[0:5]))
plt.xlabel("IPL teams")
plt.ylabel("No.of matchs")
plt.title("IPL TOP 5 TEAMS")
plt.grid(True)
plt.show()


# In[22]:


plt.figure(figsize=(10,6))
plt.bar(list(ipl['match_winner'].value_counts()[0:3].keys()),list(ipl['match_winner'].value_counts()[0:3]),color=["blue","yellow","violet"])
plt.xlabel("IPL teams")
plt.ylabel("No.of matchs")
plt.title("IPL TOP 5 TEAMS")
plt.grid(True)
plt.show()


# In[23]:


plt.figure(figsize=(15,15))
plt.pie(list(ipl['match_winner'].value_counts()),labels=list(ipl['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[24]:


second_batting=ipl[ipl['Win_Type']!='runs']
second_batting.head()


# In[25]:


plt.hist(second_batting['Win_Margin'],bins=30)
plt.show()


# In[26]:


second_batting['match_winner'].value_counts()


# In[27]:


plt.figure(figsize=(7,7))
plt.bar(list(second_batting['match_winner'].value_counts().keys()[0:4]),list(second_batting['match_winner'].value_counts()[0:4]),color=["red","green","yellow","blue"])
plt.show()


# In[28]:


plt.figure(figsize=(7,7))
plt.pie(list(second_batting['match_winner'].value_counts()),labels=list(second_batting['match_winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[29]:


ipl['Season_Year'].value_counts()


# In[30]:


ipl['City_Name'].value_counts()


# In[31]:


import numpy as np


# In[32]:


np.sum(ipl['Toss_Winner']==ipl['match_winner'])


# In[33]:


324/637


# In[34]:


BBB=pd.read_csv('F:\Ball_By_Ball.csv')
BBB.head()


# In[35]:


BBB


# In[36]:


BBB['MatcH_id'].unique()


# In[37]:


match_1=BBB[BBB['MatcH_id']==598028]
match_1.head()


# In[38]:


match_1.shape


# In[39]:


RR=match_1[match_1['Innings_No']==1]


# In[47]:


RR.head()


# In[48]:


RR['Runs_Scored'].value_counts()


# In[52]:


RCB=match_1[match_1['Innings_No']==2]


# In[53]:


RCB


# In[55]:


RCB['Runs_Scored'].value_counts()


# In[ ]:




