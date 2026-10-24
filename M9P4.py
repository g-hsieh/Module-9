def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def GrossPay(payRate, hours):
    if hours <= 40:
        return payRate * hours
    else:
        regularPay = 40 * payRate
        overtimePay = (hours - 40) * (payRate * 1.5)
        return regularPay + overtimePay

def display_result(lastName, jobCode, hours, payRate, grossPay):
    print("\nEmployee Information")
    print(f"Last Name: {lastName}")
    print(f"Job Code: {jobCode.upper()}")
    print(f"Pay Rate: ${payRate:,.2f}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Gross Pay: ${grossPay:,.2f}")

employeeCount = 0
totalGrossPay = 0

runProgram = input(
    "Would you like to enter a last name to find out the job code and hours worked? (Y/N): "
)

while runProgram.lower() in ("y", "yes"):

    lastName = get_lastName()
    jobCode = input("What's the job code? ")
    hours = float(input("How many hours did you work? "))

    if jobCode.upper() == "L":
        payRate = 25.00
    elif jobCode.upper() == "A":
        payRate = 30.00
    elif jobCode.upper() == "J":
        payRate = 50.00
    else:
        print("Invalid Job Code")
        runProgram = input(
            "\nWould you like to enter another employee? (Y/N): "
        )
        continue

    grossPay = GrossPay(payRate, hours)

    employeeCount += 1
    totalGrossPay += grossPay

    display_result(lastName, jobCode, hours, payRate, grossPay)

    runProgram = input(
        "\nWould you like to enter another employee? (Y/N): "
    )

print("\nProgram Ended")
print(f"Employees Entered: {employeeCount}")
print(f"Total Gross Pay: ${totalGrossPay:,.2f}")