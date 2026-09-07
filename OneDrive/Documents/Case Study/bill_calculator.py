# Step 1: Ask the user for the price of one item and the quantity
price_str = input("Enter the price of one item: ")
quantity_str = input("Enter the quantity you want: ")

# Step 2: Convert the inputs from strings to numeric types
price = float(price_str)
quantity = int(quantity_str)

# Step 3: Calculate the total
total = price * quantity

# Step 4: Print a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")