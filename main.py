import pandas as pd

# Load your data
sales = pd.read_csv('data/Bakery Sales.csv')
prices = pd.read_csv('data/Bakery price.csv')

print("Sales Data:")
print(sales.head())

print("\nPrice Data:")
print(prices.head())