import pandas as pd
import os

# Example 1: DataFrame creation and filtering
df = pd.DataFrame({
    "Product": ["Apple", "Banana", "Orange", "Pear"],
    "Price": [3.5, 2.0, 4.0, 3.0],
    "InStock": [True, False, True, True]
})
print("Products in stock:")
print(df[df["InStock"] == True])

# Example 2: Grouping and aggregation
sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South"],
    "Revenue": [1000, 1500, 1100, 1700]
})
print("\nTotal revenue by region:")
print(sales.groupby("Region")["Revenue"].sum())

# Example 3: Import from CSV and calculate average
print("\n")
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "sales.csv")
df = pd.read_csv(csv_path)

print(df.head())
print("Average sales:", df["Sales"].mean())