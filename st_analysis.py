import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
try:
    df = pd.read_csv("C:\\Users\\ManMis\\Downloads\\Student-Enrollment-Data - Sheet1.csv")
    print("File loaded successfully")
except Exception as e:
    print(f"Error: {e}")

# Inspect the data
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Data visualization
sns.histplot(df['Total Undergraduate'])
plt.title("Distribution of Total Undergraduate Students")
plt.show()
sns.boxplot(x='Faculty', y='Total Undergraduate', data=df)
plt.title("Boxplot of Total Undergraduate Students by Faculty")
plt.xticks(rotation=90)
plt.show()

# Bar chart
fig = px.bar(df, x='Department', y='Total Undergraduate', color='Faculty', title='Undergraduate Enrollment by Department and Faculty')
fig.show()

# Pie chart
fig = px.pie(df, values='Grand Total', names='Faculty', title='Total Enrollment by Faculty')
fig.show()
