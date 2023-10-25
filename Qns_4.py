# Import necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt

# Read the student data from a CSV file and store it in a DataFrame
data = pd.read_csv('student.csv')

# Select only the columns related to 'studytime' and 'grade'
data = data[['studytime', 'grade']]

# Group the data by 'studytime' and calculate the mean grade for each group
data2 = data.groupby('studytime').mean().reset_index()

# Display the resulting DataFrame to view the calculated mean grades
print(data2)

# Extract the 'studytime' levels and mean grade values from the data2 DataFrame
study_time_levels = data2['studytime']
mean_grades = data2['grade']

# Create a line plot to visualize the average grades for different 'studytime' levels
plt.plot(study_time_levels, mean_grades, marker='o', linestyle='-')

# Add labels to the x and y axes
plt.xlabel('Study Time (1 = <2 hours, 2 = 2-5 hours, 3 = 5-10 hours, 4 = >10 hours)')
plt.ylabel('Average Grade')

# Add a title to the plot
plt.title('Average Grade by Study Time')

# Display the line plot
plt.grid(True)  # Add grid lines
plt.show()
