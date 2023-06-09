price = float(input("Enter the price of the product: "))

if price > 1000:
    product_discount = 0.1
elif price > 500:
    product_discount = 0.05
elif price > 100:
    product_discount = 0.03
else:
    product_discount = 0

sum = price * product_discount
total_price = price - sum

print(f"The total cost of the product with a discount: {total_price:.2f} $")