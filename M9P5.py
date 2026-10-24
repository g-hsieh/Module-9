def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def get_districtCode():
    districtCode = ("What's the district code? ")
    return districtCode

def get_creditHours():
    creditHours = ("How many credit hours did you take? ")
    return creditHours

def Tuition(ratePerCredit, creditHours):
    return ratePerCredit * creditHours

def display_result(lastName, districtCode, creditHours, Tuition):
    print("\nEmployee Information")
    print(f"Last Name: {lastName}")
    print(f"Tuition: ${Tuition:,.2f}")

studentCount = 0
totalTuition = 0

runProgram = input(
    "Would you like to enter a last name to find out the district and credit hours taken? (Y/N): "
)

while runProgram.lower() in ("y", "yes"):

    lastName = input("What is your last name? ")
    districtCode = input("What's the district code? ")
    creditHours = float(input("How many credit hours did you take? "))

    if districtCode.upper() == "I":
        payRate = 250.00
    elif districtCode.upper() == "O":
        payRate = 500.00
    else:
        print("Invalid District Code")
        runProgram = input(
            "\nWould you like to enter another student? (Y/N): "
        )
        continue

    tuition = Tuition(payRate, creditHours)

    studentCount += 1
    totalTuition += tuition

    print("\nStudent Information")
    print(f"Last Name: {lastName}")
    print(f"Tuition Owed: ${tuition:,.2f}")

    runProgram = input(
        "\nWould you like to enter another student? (Y/N): "
    )

print("\nProgram Ended")
print(f"Students Entered: {studentCount}")
print(f"Total Tuition Owed: ${totalTuition:,.2f}")