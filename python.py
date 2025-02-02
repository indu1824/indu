# Data Analysis Project: Student Exam Scores

# *Introduction:*
# This project analyzes a dataset of student exam scores to answer specific questions about student performance.
# The analysis uses Python libraries like pandas, NumPy, and matplotlib.

# *1. Data Loading*

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("student-mat.csv")

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# *2. Data Exploration*

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Display column data types
print("\nData types of each column:")
print(df.dtypes)

# Understand the dataset's size
print("\nShape of the dataset (rows, columns):")
print(df.shape)

# *3. Data Cleaning*

# Handle missing values (if any - there are none in this dataset, but this is good practice)
# For demonstration, if we HAD missing values in 'studytime', we'd fill with the median:
# df['studytime'].fillna(df['studytime'].median(), inplace=True)

# Remove duplicate entries
print("\nNumber of duplicate rows before removal:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Number of duplicate rows after removal:", df.duplicated().sum())

# *4. Data Analysis Questions*

# 1. What is the average score in math (G3)?
average_g3 = df['G3'].mean()
print(f"\nAverage score in math (G3): {average_g3:.2f}")

# 2. How many students scored above 15 in their final grade (G3)?
students_above_15 = df[df['G3'] > 15].shape
print(f"Number of students scoring above 15 in G3: {students_above_15}")

# 3. Is there a correlation between study time (studytime) and the final grade (G3)?
correlation = df['studytime'].corr(df['G3'])
print(f"Correlation between study time and G3: {correlation:.2f}")

# 4. Which gender has a higher average final grade (G3)?
average_g3_by_gender = df.groupby('sex')['G3'].mean()
print("\nAverage G3 score by gender:")
print(average_g3_by_gender)

# *5. Data Visualization*

# 1. Histogram of final grades (G3)
plt.figure(figsize=(8, 6))
plt.hist(df['G3'], bins=10, edgecolor='black')
plt.title('Distribution of Final Grades (G3)')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.show()
#Key Finding: The histogram shows the distribution of final grades. Observe the shape of the distribution (e.g., normal, skewed) and identify any common grade ranges.


# 2. Scatter plot between study time (studytime) and final grade (G3)
plt.figure(figsize=(8, 6))
plt.scatter(df['studytime'], df['G3'])
plt.title('Scatter Plot of Study Time vs. Final Grade (G3)')
plt.xlabel('Study Time (hours/week)')
plt.ylabel('Final Grade (G3)')
plt.show()
#Key Finding: The scatter plot helps visualize the relationship between study time and final grade. Look for patterns or trends; a positive correlation would suggest that more study time is associated with higher grades.

# 3. Bar chart comparing the average scores of male and female students
plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='G3', data=df) #Seaborn makes this easier!
plt.title('Average Final Grade (G3) by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.show()
#Key Finding: The bar chart directly compares the average final grades between male and female students.  This makes it easy to see if one gender tends to perform better than the other.


# *Analysis Summary:*

# * Data Loading: The dataset was successfully loaded using pandas.
# * Data Exploration: The exploration revealed the data types and size of the dataset.  No missing values were found.
# * Data Cleaning: Duplicate rows were removed to ensure data integrity.
# * Data Analysis: The average G3 score, the number of students scoring above 15, the correlation between study time and G3, and the average G3 scores by gender were calculated.
# * Data Visualization:  Histograms, scatter plots, and bar charts were used to visualize the distribution of grades, the relationship between study time and grades, and the comparison of average grades by gender.

# *Key Findings:*

# * The average G3 score was calculated.
# * The number of students achieving a G3 score above 15 was determined.
# * The correlation between study time and G3 was analyzed.
# * The difference in average G3 scores between genders was visualized and analyzed.  (Remember to state the actual findings from your analysis here after running the code.)  For example: "Females had a slightly higher average G3 score than males."
# * The visualizations provided insights into the distribution of grades and the relationships between variables.  (Summarize what the graphs show here.) For example: "The histogram showed a roughly normal distribution of G3 grades."  "The scatter plot suggested a weak positive correlation between study time and G3."

# *Conclusion:*

# This project provided a comprehensive analysis of the student exam scores dataset. The insights gained can be used to understand factors influencing student performance.  (You can add more concluding remarks based on your findings.)
