# customers.py
# Author: Aleena Khan
# Module 11 Lab: Customer Dictionary & Lookup


# Exercise 1
print("---Exercise 1---")
customer = {
    "name": "Alice", # key: value,
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer['ytd_spend'])

print(customer)


# Exercise 2
print("---Exercise 2---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum' # Updating the value of an existing key
print(customer)
del customer['email']
print(customer)
# print(customer.get("Name", "Key Not Found"))
# print(customer.get('ytd_spend', 0)) # the , 0 is if there is nothing to give out


# Exercise 3
print("---Exercise 3---")
print(customer.get("email", "no email on file"))


# Exercise 4
print("---Exercise 4---")

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

# Looping over customer directly gives only the keys so I have to look up each value with customer[something]. Using items() gives me the key and value together in one step.

# try:
#     print(customer['email'])
# except KeyError as error:
#     print("KeyError caught: ", error)


# Exercise 5
print("---Exercise 5---")

tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15
                  }

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer["tier"]}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


# Exercise 6
print("---Exercise 6---")

customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carol", "tier": "bronze"}
]
for record in customers:
    rate = tier_discounts.get(record["tier"], 0) 
    discount = 300 * rate
    print(f"{record["name"]} ({record["tier"]}): ${discount:.2f} off a $300 purchase")


# Exercise 7
print("---Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details["stock"]} left")


# Exercise 8
print("---Exercise 8---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")


# Reflection
# 1. I'd use bracket notation when a key has to exist, like customer["name"], because a missing key means something is broken and I want the KeyError to show it. I'd use .get() when a key might be missing and a default is fine, like looking up a tier discount or accumulating totals. My rule of thumb is if a missing key is a bug, use brackets; if it's expected, use .get().
# 2. The summary dictionary in Exercise 8 reminds me of a PivotTable or a SUMIF in Excel, since both total values by category. The Python version is more useful for large datasets because it handles far more rows than Excel, and I can rerun the same script on new data instead of rebuilding thepivot by hand each time.