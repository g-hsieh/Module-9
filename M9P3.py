def get_destinationCity():
    destinationCity = input("What is your destination city? ")
    return destinationCity

def get_mpg(miles, gallons):
    return miles / gallons

def display_result(destinationCity, miles, gallons, milesPerGallon):
    print("\nDestination City:", destinationCity)
    print("Number of miles travelled:", miles)
    print("Number of gallons used:", gallons)
    print(f"Miles per gallon: {milesPerGallon:.2f}")

entryCount = 0

runProgram = input(
    "Would you like to enter a destination city to find out how many miles travelled and gallons used? (Y/N): "
)

while runProgram.lower() in ("y", "yes"):

    destinationCity = get_destinationCity()
    miles = float(input("How many miles did you travel? "))
    gallons = float(input("How many gallons did you use? "))

    if gallons == 0:
        print("Gallons used cannot be zero.")
    else:
        milesPerGallon = get_mpg(miles, gallons)

        entryCount += 1

        display_result(destinationCity, miles, gallons, milesPerGallon)

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
