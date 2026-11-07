import pandas as pd

df = pd.read_excel("Grocery_Sales_Analysis.xlsx")
print(df.columns.tolist())

df.columns = df.columns.astype(str).str.strip()
print([repr(col) for col in df.columns])

print(df)

print(df.columns.tolist())
print(df.head())

    



print(repr(df.columns.tolist()))
print(df.columns.tolist())

df.columns = df.columns.str.strip().str.lower()

df["total_sales"] = pd.to_numeric(df["total_sales"],
                                  errors="coerce")

total_revenue = df["total_sales"].sum()

print("Total Revenue:",
      total_revenue)

print("Highest Sale:",
      df["total_sales"].max())

print("Average Sales:",
      df["total_sales"].mean())


product_sales = df.groupby("product")["total_sales"].sum()

print("Product Wise Sales:")
print(product_sales)

import matplotlib.pyplot as plt

product_sales.plot(kind="bar")

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

city_sales = df.groupby("city")["total_sales"].sum()

print("City Wise Sales:")
print(city_sales)

category_sales = df.groupby("category")["total_sales"].sum()

print("Category Wise Sales:")
print(category_sales)


quantity_sales = df.groupby("category")["quantity"].sum()

print("Quantity Wise Sales:")
print(quantity_sales)

quantity_sales.plot(kind="bar")

plt.title("Quantity Wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Quantity")
plt.show()

city_sales.plot(kind="bar")
plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.savefig("Product_Wise_Sales.png")

plt.show()

product_sales = df.groupby("product")["total_sales"].sum()

print("Product Wise Sales")
print(product_sales)

product_sales.plot(kind="bar")
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
plt.show()
plt.show()
