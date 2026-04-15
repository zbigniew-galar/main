import pandas as pd

# Load data
file_path = "src/input_data/Sales.xlsx"
df = pd.read_excel(file_path)

# Ensure correct column names
df.columns = ["SKU", "Date", "Sales"]

# Convert Sales to numeric (handle commas if needed)
df["Sales"] = (
    df["Sales"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Aggregate total sales per SKU
sku_sales = df.groupby("SKU", as_index=False)["Sales"].sum()

# Sort by sales descending
sku_sales = sku_sales.sort_values(by="Sales", ascending=False)

# Calculate cumulative percentage
total_sales = sku_sales["Sales"].sum()
sku_sales["Cumulative_Sales"] = sku_sales["Sales"].cumsum()
sku_sales["Cumulative_%"] = sku_sales["Cumulative_Sales"] / total_sales * 100

# Assign ABC categories
def classify_abc(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

sku_sales["ABC_Class"] = sku_sales["Cumulative_%"].apply(classify_abc)

# Save result
output_path = "src/input_data/ABC_Analysis.xlsx"
sku_sales.to_excel(output_path, index=False)

# Print preview
print(sku_sales.head())
