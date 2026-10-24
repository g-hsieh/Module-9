def get_lastName():
    lastName = input("What is your last name? ")
    return lastName

def calculateBatAverage(num_hits, num_bats):
    batAverage = num_hits / num_bats
    return batAverage

def display_result(lastName, num_hits, num_bats, batAverage):
    print("\nLast Name:", lastName)
    print("Number of hits:", num_hits)
    print("Number of bats:", num_bats)
    print(f"Batting Average: {batAverage:.3f}")

totalAverage = 0
playerCount = 0

runProgram = input("Would you like to enter player data? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    lastName = get_lastName()
    num_hits = int(input("How many hits did you have? "))
    num_bats = int(input("How many times at bat? "))

    average = calculateBatAverage(num_hits, num_bats)

    totalAverage += average
    playerCount += 1

    display_result(lastName, num_hits, num_bats, average)

    runProgram = input(
        "\nWould you like to enter another player's hits and bats? (Y/N): "
    )

print("\nProgram ended.")
print(f"Number of players entered: {playerCount}")

if playerCount > 0:
    overallAverage = totalAverage / playerCount
    print(f"The batting average for {playerCount} players is {overallAverage:.3f}")
else:
    print("No players were entered.")