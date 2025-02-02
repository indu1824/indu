import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student-mat.csv")
print("First 5 rows of the dataset:")
print(df.head())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nData types of each column:")
print(df.dtypes)
print("\nShape of the dataset (rows, columns):")
print(df.shape)
print("\nNumber of duplicate rows before removal:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("Number of duplicate rows after removal:", df.duplicated().sum())
average_g3 = df['G3'].mean()
print(f"\nAverage score in math (G3): {average_g3:.2f}")
students_above_15 = df[df['G3'] > 15].shape
print(f"Number of students scoring above 15 in G3: {students_above_15}")
correlation = df['studytime'].corr(df['G3'])
print(f"Correlation between study time and G3: {correlation:.2f}")
average_g3_by_gender = df.groupby('sex')['G3'].mean()
print("\nAverage G3 score by gender:")
print(average_g3_by_gender)
plt.figure(figsize=(8, 6))
plt.hist(df['G3'], bins=10, edgecolor='black')
plt.title('Distribution of Final Grades (G3)')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.show()
plt.figure(figsize=(8, 6))
plt.scatter(df['studytime'], df['G3'])
plt.title('Scatter Plot of Study Time vs. Final Grade (G3)')
plt.xlabel('Study Time (hours/week)')
plt.ylabel('Final Grade (G3)')
plt.show()
plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='G3', data=df) 
plt.title('Average Final Grade (G3) by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.show()

