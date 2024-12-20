import pandas as pd
import matplotlib.pyplot as plt

# Load the California and New York drought data
california_data = pd.read_csv('USDM-california.csv')
new_york_data = pd.read_csv('tableExport.csv')

# Convert date columns to datetime format
california_data['MapDate'] = pd.to_datetime(california_data['MapDate'], format='%Y%m%d')
new_york_data['Date'] = pd.to_datetime(new_york_data['Date'])

# Merge datasets on date for alignment
merged_data = pd.merge(california_data, new_york_data, left_on='MapDate', right_on='Date', how='inner')

# Check for missing or misaligned data
if merged_data.empty:
    print("Merged dataset is empty. Check date formats or data alignment.")
else:
    # Calculate correlation between California D0 and New York D0-D4
    correlation = merged_data['D0'].corr(merged_data['D0-D4'])
    print(f"Correlation between California D0 and New York D0-D4: {correlation}")

    # Plot the drought conditions
    plt.figure(figsize=(12, 6))
    plt.plot(merged_data['MapDate'], merged_data['D0'], label='California D0', color='blue', marker='o')
    plt.plot(merged_data['MapDate'], merged_data['D0-D4'], label='New York D0-D4', color='orange', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Drought Condition (%)')
    plt.title('Drought Conditions in California and New York')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
