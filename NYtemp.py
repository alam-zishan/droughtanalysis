#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import matplotlib.pyplot as plt

# Load the data, skipping metadata lines
data = pd.read_csv('Downloads/data.csv', skiprows=4)

# Convert the 'Date' column to datetime format for better handling
data['Date'] = pd.to_datetime(data['Date'], format='%Y%m')

# Basic statistics
summary = data.describe()
print("Summary Statistics:")
print(summary)

# Plotting the average temperature over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Value'], marker='o', label='Average Temperature')
plt.axhline(data['Value'].mean(), color='red', linestyle='--', label='Mean Temperature')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.grid()
plt.show()

# Plotting the temperature anomaly over time
plt.figure(figsize=(10, 6))
plt.bar(data['Date'], data['Anomaly'], color='orange', label='Temperature Anomaly')
plt.axhline(0, color='black', linestyle='--')
plt.title('Temperature Anomaly Over Time')
plt.xlabel('Date')
plt.ylabel('Anomaly (°F)')
plt.legend()
plt.grid()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




