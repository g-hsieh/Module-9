def mpg(miles, gallons):
    return miles / gallons

entryCount = 0

runProgram = input(
    "Would you like to enter a destination city to find out how many miles travelled and gallons used? (Y/N): "
)

while runProgram.lower() in ("y", "yes"):

    destinationCity = input("What is your destination city? ")
    miles = float(input("How many miles did you travel? "))
    gallons = float(input("How many gallons did you use? "))

    milesPerGallon = mpg(miles, gallons)

    entryCount += 1

    print("\nDestination City:", destinationCity)
    print("Number of miles travelled:", miles)
    print("Number of gallons used:", gallons)
    print(f"Miles per gallon: {milesPerGallon:.2f}")

    runProgram = input(
        "\nWould you like to enter another destination city? (Y/N): "
    )

print("\nProgram ended.")
print(f"Number of entries entered: {entryCount}")

if entryCount > 0:
    print(
        f"You travelled to {destinationCity} at approximately "
        f"{milesPerGallon:.2f} miles per gallon."
    )
else:
    print("No entries were entered.")