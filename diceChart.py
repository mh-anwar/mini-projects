maxNum = input("Enter maximum for dice chart: ")

relativeMax = int(maxNum)
startNum = 0

while startNum < int(maxNum):
    for i in range(startNum, relativeMax + 1):
        print(f"{i:02d}".ljust(2), end="    ")
    print("\n")
    relativeMax += 1
    startNum += 1
