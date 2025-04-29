burger=5
pizza=8
coffee=3
item=input("Enter the item you want to order (Burger, Pizza, Coffee): ").lower()
quantity= int(input("Enter the quantity: "))
total_price = 0
if item == "burger":
    total_price=burger*quantity
elif item == "pizza":
    total_price=pizza*quantity
elif item == "coffee":
    total_price=coffee*quantity
else:
    print("Item Unavailable")
if total_price > 0:
    print(f"Your bill for {quantity} {item}(s) is : ${total_price}")
