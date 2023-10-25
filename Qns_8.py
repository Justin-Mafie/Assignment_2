import pandas as pd
import matplotlib.pyplot as plt

# Read the student data from a CSV file and store it in a DataFrame
data = pd.read_csv('student.csv')

# Define the two categories based on 'studytime'
category_1 = data[data['studytime'] < 3]
category_2 = data[data['studytime'] >=3]

# Create a list of the two categories for box plotting
categories = [category_1['grade'], category_2['grade']]

# Create a box plot to compare the 'grade' for each category
plt.boxplot(categories, labels=['Study Time < 3', 'Study Time >= 3'])

# Add labels and a title to the plot
plt.xlabel('Study Time Categories')
plt.ylabel('Grade')
plt.title('Box Plot of Grade by Study Time Category')

# Show the plot
plt.show()
