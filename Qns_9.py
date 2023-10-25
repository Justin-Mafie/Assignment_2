import pandas as pd

# Step 1: Load the crime data from the specified CSV file
file_path = 'https://raw.githubusercontent.com/jhueber/Crime/master/2017_Crime.csv'
crime_data = pd.read_csv(file_path)

# Step 2: Create a pandas dataframe to hold the crime data
df = pd.DataFrame(crime_data)

# Step 3: Preprocess the data by removing rows with missing values
df = df.dropna()

# Step 4: Compute the correlation of features in the crime data with the ratio of violent crimes
# Calculate the ratio of Violent Crime to Total Crime
violent_crime_rates = df['Violent Crime'] / df['Total Crime']

# Compute the correlation between each feature and the violent crime rate
correlation_results = df.corrwith(violent_crime_rates)

# Step 5: Display the correlation results
# Iterate through the columns and print the correlation results
for i in range(len(correlation_results)):
    print(f"Correlation between {df.columns[i]} and violent crime rate: {correlation_results[i]}")
