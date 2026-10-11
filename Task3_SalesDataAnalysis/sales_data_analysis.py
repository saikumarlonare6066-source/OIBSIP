import pandas as pd
import matplotlib.pyplot as plt
import os

# Load sales dataset
df = pd.read_csv("sales_data.csv")

# Convert order date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Create output folder
os.makedirs("outputs", exist_ok=True)

print("SALES DATA ANALYSIS")
print("-" * 30)

print("\nFirst 5 Orders:")
print(df.head())

print("\nTotal Revenue:")
print("Rs.", round(df["Revenue"].sum(), 2))

print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())

print("\nRevenue by Product:")
print(df.groupby("Product")["Revenue"].sum().sort_values(ascending=False))

print("\nRevenue by City:")
print(df.groupby("City")["Revenue"].sum().sort_values(ascending=False))

# Monthly sales trend
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/monthly_sales_trend.png", dpi=300)
plt.close()

# Revenue by product
product_sales = df.groupby("Product")["Revenue"].sum().sort_values()

plt.figure(figsize=(9, 5))
product_sales.plot(kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue (Rs.)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("outputs/revenue_by_product.png", dpi=300)
plt.close()

# Revenue by city
city_sales = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
city_sales.plot(kind="bar")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/revenue_by_city.png", dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print("Graphs saved in the outputs folder.")