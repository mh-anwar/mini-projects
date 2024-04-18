rounds = int(input("Enter number of rounds: "))

from itertools import product

combinations = list(map(list, product("WL", repeat=rounds)))
print("Game with {} rounds - where each round player can Win or Loose".format(rounds))
print("Total Number of Combinations:", len(combinations))
# Print the combinations
for combo in combinations:
    tempArr = []
    # Calculate from 8/104
    totalProbability = 1;
    # start 1 higher, because it deducts 1
    numerator = 9;
    denominator = 55;
    for possibility in combo:
        if possibility == "W":
            numerator -= 1
            denominator -= 1
        else:
            denominator -= 1

        newPossbility = numerator/denominator

        tempArr.append(f"{numerator}/{denominator}")
        totalProbability *= newPossbility
        #combinations[combinations.index(combo)][combo.index(possibility)] = newPossbility
  
    print(f"P({', '.join(combo)}): {round(totalProbability*100, 12)}% ".ljust(3),end='    ')
    print( f"Cards Left {numerator} / {denominator}".ljust(2),end='    ') 
    print(f"{' x '.join(tempArr)}")

    # Total Loss Incurred: $ + {numerator - 8 * 2