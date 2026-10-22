def calculateTotal(quantity, price):
    total = quantity * price
    return total

print("Decide if you would like to enter quantities and prices inside the loop.")
print()

runProgram = input("Would you like to know the quantities and prices? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    quantity = int(input("Enter the quantity: "))
    price = float(input("What's the price? "))

    total = calculateTotal(quantity, price)

    if total >= 10000:
        discountAmount = total * 0.10
    else:
        discountAmount = 0

    print("\nQuantity:", quantity)
    print(f"Price: ${price:,.2f}")
    print(f"Total: ${total:,.2f}")
    print(f"Discount: ${discountAmount:,.2f}")

    runProgram = input("\nWould you like to enter another quantity and price? (Y/N): ")

print("\nProgram ended.")