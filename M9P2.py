def bat_Average(num_hits, num_bats):
    return num_hits / num_bats

totalAverage = 0
playerCount = 0

runProgram = input("Would you like to enter player data? (Y/N): ")

while runProgram.lower() in ("y", "yes"):

    lastName = input("What is your last name? ")
    num_hits = int(input("How many hits did you have? "))
    num_bats = int(input("How many times at bat? "))

    Average = bat_Average(num_hits, num_bats)

    totalAverage += Average
    playerCount += 1

    print("\nLast Name:", lastName)
    print(f"Batting Average: {Average:.3f}")

    runProgram = input("\nWould you like to enter another player's hits and bats? (Y/N): ")

print("\nProgram ended.")
print(f"Number of players entered: {playerCount}")

if playerCount > 0:
    overallAverage = totalAverage / playerCount
    print(f"The batting average for {playerCount} players is {overallAverage:.3f}")
else:
    print("No players were entered.")