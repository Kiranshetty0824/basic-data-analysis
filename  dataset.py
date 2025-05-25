import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/sample.csv")

# Show basic information
print("First 5 rows:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Data Cleaning (drop rows with missing values)
df_clean = df.dropna()

# Plot: Histogram of a numeric column
plt.figure(figsize=(8, 5))
sns.histplot(df_clean['column_name'], kde=True)
plt.title('Distribution of column_name')
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()

# Plot: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df_clean.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
