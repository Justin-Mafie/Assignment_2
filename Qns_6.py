

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Assuming you have your crime data in a DataFrame
# Load your data (replace 'crime_data.csv' with the actual file path)
data = pd.read_csv('crime.csv')

# Step 3: Create a scatter plot of the original data
plt.figure(figsize=(10, 6))
plt.scatter(data['PctPopUnderPov'], data['ViolentCrimesPerPop'], alpha=0.5)
plt.title('Original Data')
plt.xlabel('PctPopUnderPov')
plt.ylabel('ViolentCrimesPerPop')
plt.grid()

# Step 4: Scale the feature values using MinMaxScaler
scaler = MinMaxScaler()
scaled_data = data[['PctPopUnderPov', 'ViolentCrimesPerPop']]
scaled_data = scaler.fit_transform(scaled_data)

# Step 5: Create a scatter plot with the scaled values
plt.figure(figsize=(10, 6))
plt.scatter(scaled_data[:, 0], scaled_data[:, 1], alpha=0.5)
plt.title('Scaled Data')
plt.xlabel('Scaled PctPopUnderPov')
plt.ylabel('Scaled ViolentCrimesPerPop')
plt.grid()

plt.show()
