import pandas as pd
import matplotlib.pyplot as plt

# Load the water consumption data for New York City and San Jose
nyc_data = pd.read_csv('Water_Consumption_in_the_City_of_New_York.csv')
san_jose_data = pd.read_csv('San_Jose_Water_Consumption.csv')

# Extract relevant columns for plotting
nyc_years = nyc_data['Year']
nyc_per_capita = nyc_data['Per Capita(Gallons per person per day)']

san_jose_years = san_jose_data['Year']
san_jose_per_capita = san_jose_data['Per Capita (Gallons per person per day)']

# Plot the per capita water consumption trends
plt.figure(figsize=(12, 6))

plt.plot(nyc_years, nyc_per_capita, label='NYC Per Capita Water Consumption', color='blue', marker='o')
plt.plot(san_jose_years, san_jose_per_capita, label='San Jose Per Capita Water Consumption', color='green', marker='o')

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Per Capita Water Consumption (Gallons per person per day)')
plt.title('Per Capita Water Consumption Trends: NYC vs San Jose')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
