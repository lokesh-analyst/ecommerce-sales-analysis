import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")

# Load Dataset (adjust path if needed)
df = pd.read_csv("data\superstore.csv", encoding="latin1")
df.head()

# Data Cleaning
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Category'] = df['Category'].str.title()
df.info()

# Exporatory Data Analysis (EDA) & Visualization
# Sales by Region
sales_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=sales_region.index, y=sales_region.values)
plt.title("Total Sales by Region")
plt.show()

# Top 10 Profitable Products
top_products = df.groupby('Product Name')['Profit'].sum().nlargest(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title("Top 10 Profitable Products")
plt.show()

# Monthly Sales Trend
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.plot(kind='line', marker='o', figsize=(12,6), title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.show()