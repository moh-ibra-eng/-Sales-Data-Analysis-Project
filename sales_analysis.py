import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# 1️⃣ Load Data
# ===============================
df = pd.read_csv(
    r"C:\Users\DELL\Desktop\py4e\files\csv_file\Data Analysis projects\Sample - Superstore.csv.zip",
    encoding="latin1"
)

# ===============================
# 2️⃣ Initial Exploration
# ===============================
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ===============================
# 3️⃣ Data Cleaning
# ===============================
df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# ===============================
# 4️⃣ Feature Engineering
# ===============================
df["Profit Margin"] = df["Profit"] / df["Sales"]
df["Month"] = df["Order Date"].dt.to_period("M")

# ===============================
# 5️⃣ Key Metrics
# ===============================
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\nKPIs:")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))

# ===============================
# 6️⃣ Analysis
# ===============================

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# Profit by Category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nProfit by Category:")
print(category_profit)

# Average Profit Margin by Region
profit_margin_region = df.groupby("Region")["Profit Margin"].mean().sort_values(ascending=False)
print("\nAverage Profit Margin by Region:")
print(profit_margin_region)

# Top 5 Products by Sales
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products by Sales:")
print(top_products)

# Worst 5 Products by Profit
worst_products = df.groupby("Product Name")["Profit"].sum().sort_values().head(5)
print("\nWorst 5 Products by Profit:")
print(worst_products)

# Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()

# ===============================
# 7️⃣ Visualization
# ===============================

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.savefig("images/sales_by_region.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar", color="orange")
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.savefig("images/profit_by_category.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("images/monthly_sales_trend.png", bbox_inches="tight")
plt.show()

# ===============================
# 8️⃣ Final Message
# ===============================
print("\nAnalysis Completed Successfully ✅")




