# Task 5: Data Analysis on CSV Files
# Tools: Python, Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# 1. Create sample CSV data directly inside the notebook
csv_data = """Product,Month,Sales
A,Jan,200
B,Jan,150
C,Jan,300
A,Feb,250
B,Feb,100
C,Feb,400
A,Mar,300
B,Mar,200
C,Mar,350
"""

# 2. Load the CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# 3. Basic insights
print("First 5 rows:\n", df.head())
print("\nShape of data:", df.shape)
print("\nSummary statistics:\n", df.describe())

# 4. Group & Aggregate
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:\n", sales_by_product)

sales_by_month = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales Trend:\n", sales_by_month)

# 5. Visualization
# Bar chart for product sales
plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar", color="skyblue", title="Total Sales by Product")
plt.ylabel("Sales")
plt.xlabel("Product")
plt.show()

# Line chart for monthly sales
plt.figure(figsize=(8,5))
sales_by_month.plot(kind="line", marker="o", color="green", title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.show()
