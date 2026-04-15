import pandas as pd
import numpy as np

# =========================
# CONFIGURATION & MAPPING
# =========================
sales_file = "src/input_data/Sales.xlsx"
output_file = "src/output_data/ABC_XYZ_Analysis.xlsx"

# Hardcoded mapping from image
# Format: "Segment": ("Animal", "Policy")
SEG_DATA = {
    "AX": ("Horses", "MTS"),
    "AY": ("Mad Bulls", "MTS"),
    "AZ": ("Mad Bulls", "MTS"),
    "BX": ("Horses", "MTS"),
    "BY": ("Mad Bulls", "MTS"),
    "BZ": ("Mad Bulls", "MTO"),
    "CX": ("Turtles", "MTS"),
    "CY": ("Rabbits", "MTO"),
    "CZ": ("Rabbits", "MTO")
}

# =========================
# DATA LOADING & CLEANING
# =========================
df = pd.read_excel(sales_file)
df.columns = ["SKU", "Date", "Sales"]
df["Sales"] = df["Sales"].astype(str).str.replace(",", ".", regex=False).astype(float)
df["Date"] = pd.to_datetime(df["Date"])

# =========================
# ABC ANALYSIS (Revenue)
# =========================
sku_sales = df.groupby("SKU")["Sales"].sum().reset_index().sort_values("Sales", ascending=False)
cum_pct = (sku_sales["Sales"].cumsum() / sku_sales["Sales"].sum()) * 100
sku_sales["ABC"] = np.select(
    [cum_pct <= 80, cum_pct <= 95], 
    ["A", "B"], 
    default="C"
)

# =========================
# XYZ ANALYSIS (Variability)
# =========================
# Calculation: $$CV = \frac{\sigma}{\mu}$$
stats = df.groupby("SKU")["Sales"].agg(["mean", "std"]).reset_index()
stats["CV"] = stats["std"] / stats["mean"]
stats["XYZ"] = np.select(
    [stats["CV"] <= 0.5, stats["CV"] <= 1.0], 
    ["X", "Y"], 
    default="Z"
)

# =========================
# MERGE & HARDCODE SEGMENTS
# =========================
result = pd.merge(sku_sales[["SKU", "Sales", "ABC"]], stats[["SKU", "XYZ"]], on="SKU")
result["Segment"] = result["ABC"] + result["XYZ"]

# Apply hardcoded Animal and Policy logic
result["Animal"] = result["Segment"].map(lambda x: SEG_DATA.get(x, (None, None))[0])
result["Policy"] = result["Segment"].map(lambda x: SEG_DATA.get(x, (None, None))[1])

# =========================
# EXPORT
# =========================
result.sort_values("Sales", ascending=False).to_excel(output_file, index=False)
print(f"File saved: {output_file}")
