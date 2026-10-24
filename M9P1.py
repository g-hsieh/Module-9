def get_quantity():
    quantity = int(input("Enter the quantity: "))
    return quantity

def calculateTotal(quantity, price):
    total = quantity * price
    return total

def calculateExtPrice(quantity, price):
    ExtPrice = quantity * price
    return ExtPrice

def calculateTotalExtPrice(total, discountAmount):
    totalExtPrice = total - discountAmount
    return totalExtPrice

def display_result(quantity, price, total, discountAmount, ExtPrice, totalExtPrice):
    print("\nQuantity:", quantity)
    print(f"Price: ${price:,.2f}")
    print(f"Total: ${total:,.2f}")
    print(f"Discount: ${discountAmount:,.2f}")
    print(f"Extended Price: ${ExtPrice:,.2f}")
    print(f"Net Extended Price: ${totalExtPrice:,.2f}")

print("Decide if you would like to enter quantities and prices inside the loop.")
print()

runProgram = input("Would you like to know the quantities and prices? (Y/N): ")

grandTotalExtPrice = 0

while runProgram.lower() in ("y", "yes"):

    quantity = get_quantity()
    price = float(input("What's the price? "))

    total = calculateTotal(quantity, price)
    ExtPrice = calculateExtPrice(quantity, price)

    if total >= 10000:
        discountAmount = total * 0.10
    else:
        discountAmount = 0

    totalExtPrice = calculateTotalExtPrice(total, discountAmount)
    grandTotalExtPrice += totalExtPrice

    display_result(
        quantity,
        price,
        total,
        discountAmount,
        ExtPrice,
        totalExtPrice
    )

    runProgram = input("\nWould you like to enter another quantity and price? (Y/N): ")

print("\nProgram ended.")
print(f"The Total Extended Price for all items is ${grandTotalExtPrice:,.2f}")