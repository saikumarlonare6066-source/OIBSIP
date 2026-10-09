
import pandas as pd
import seaborn as sns
# Load the retail sales dataset
df = pd.read_csv("OnlineRetail.csv", encoding="latin1")

# Display the first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())





# Descriptive statistics
print("\nDESCRIPTIVE STATISTICS:")
print(df.describe())

# Column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Data types
print("\nDATA TYPES:")
print(df.dtypes)






# Check duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Check missing values in each column
print("\nMISSING VALUES BEFORE CLEANING:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows without essential sales information
df = df.dropna(subset=["InvoiceNo", "StockCode", "Quantity", "UnitPrice"])

# Keep only positive quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

print("\nDATA SHAPE AFTER CLEANING:")
print(df.shape)

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())




# Calculate sales revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("\nTOTAL SALES REVENUE:")
print(round(df["Revenue"].sum(), 2))

print("\nTOP 5 SALES RECORDS:")
print(df[["InvoiceNo", "Description", "Quantity",
          "UnitPrice", "Revenue"]].head())




import matplotlib.pyplot as plt

# Convert invoice date into datetime
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], dayfirst=True, errors="coerce"
)

# Remove records with invalid dates
df = df.dropna(subset=["InvoiceDate"])

# Calculate monthly revenue
df["Month"] = df["InvoiceDate"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

# Plot monthly sales
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()










# Top 10 products by revenue
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS BY REVENUE:")
print(top_products)

# Plot the top 10 products
plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("top_10_products.png", dpi=300)
plt.show()






# Revenue by country
country_sales = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 COUNTRIES BY REVENUE:")
print(country_sales)

# Create chart
plt.figure(figsize=(12, 6))
country_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top_10_countries.png", dpi=300)
plt.show()






# Correlation Heatmap
numeric_data = df[["Quantity", "UnitPrice", "Revenue"]]
correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Retail Sales")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()



 # Business Insights and Recommendations
print("\nBUSINESS INSIGHTS AND RECOMMENDATIONS")

print("1. Focus on products that generate high revenue.")
print("2. Monitor monthly sales trends to identify peak sales periods.")
print("3. Focus on countries with high sales revenue.")
print("4. Maintain sufficient stock for popular products.")
print("5. Use sales data to improve inventory planning.")
