# Import the necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt

# Read the student data from a CSV file and store it in a DataFrame
data = pd.read_csv('student.csv')

# Select the relevant columns for analysis: 'study-time' and 'grade'
# Make sure the column names match the column names in your CSV file
data = data[['study-time', 'grade']]
# Fixed column names

# Group the data by 'study-time' and calculate the mean grade for each group
average_grades_by_study_time = data.groupby('study-time').mean().reset_index()

# Display the resulting DataFrame to inspect the calculated mean grades
print(average_grades_by_study_time)

# Extract the 'study-time' levels and their corresponding mean grades
study_time_levels = average_grades_by_study_time['study-time']
mean_grades = average_grades_by_study_time['grade']

# Create a line plot to visualize the average grades for different 'study-time' levels
plt.plot(study_time_levels, mean_grades, marker='o', linestyle='-')

# Add labels to the x and y axes
plt.xlabel('Study Time (1 = <2 hours, 2 = 2-5 hours, 3 = 5-10 hours, 4 = >10 hours)')
plt.ylabel('Average Grade')

# Customize the appearance of the plot
plt.title('Average Grade by Study Time')
plt.grid(True)

# Display the line plot
plt.show()
