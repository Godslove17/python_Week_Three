# Discounts Calculator
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# calculate the final price after applying the discount
final_price = calculate_discount(price, discount_percent)

# print the final price after applying the discount, or if no discount was applied, print the original price of the item
if final_price!= price:
    print("The final price after applying the discount is:", final_price)
else:
    print("No discount was applied, the price remains: ", price)