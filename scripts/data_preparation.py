# Import necessary libraries
import pandas as pd

# Load sample data
data = pd.read_csv('../data/sample_data.csv')

# Display the first few rows of the data
print(data.head())

# Data preprocessing steps
# Example: Fill missing values
data.fillna(method='ffill', inplace=True)

# Save preprocessed data
data.to_csv('../data/preprocessed_data.csv', index=False)

print("Data preparation completed and saved to 'preprocessed_data.csv'.")