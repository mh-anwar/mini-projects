# Data Management Games Fair "Roulette Game" Expected Value Calculator
# This program calculates the expected value of a game from a player's perspective given
# that the player can bet $1,2 or 3 and the probabilities of winning and losing are known.
# The purpose is for the game to be unfair, and thus a negative expected value should be outputted.

# This program also assumes that the player will always lose the principal as it is the entrance fee

#  Calculate the probabilities of winning and losing for number of rounds
numSections = 20 # 20 sections on the roulette wheel
probabilityBW = 0.05 * numSections # get +100% and lose the principal
probabilityMW = 0.15 * numSections # get +50% and lose the principal
probabilitySL = 0.35 * numSections # lose 25% and lose the principal
probabilityML = 0.35 * numSections # lose 50% and lose the principal
probabilityBL = 0.1 * numSections # lose 100% and lose the principal

print(f"Probability of Winning Big: {int(probabilityBW)}/{numSections}")
print(f"Probability of Winning Mild: {int(probabilityMW)}/{numSections}")
print(f"Probability of Losing Small: {int(probabilitySL)}/{numSections}")
print(f"Probability of Losing Mild: {int(probabilityML)}/{numSections}")
print(f"Probability of Losing Big: {int(probabilityBL)}/{numSections}")
print("\n")


# Calculate the probabilities of winning and losing for each $ amount
# Principal Amount which is the amount initially invested can be $1, $2 or $3
print("Let the Random Variable X be the amount of money won or lost")
principalAmounts = [1,2,3]
# Calculate expected values
for i in principalAmounts:
    print(f"Principal Amount: ${i}")
    # Define column widths
    col_width = 15

    # Header
    print(f"{'Loss Type':<{col_width}}{'x':<{col_width}}{'P(x)':<{col_width}}{'x*P(x)':<{col_width}}")
    print(f"{'---------':<{col_width}}{'----':<{col_width}}{'------':<{col_width}}")

    # Each bracket in the expected value is: (amount * probability)
    expectedValue = (( (i) * probabilityBW)  # Double your winnings
                     + ((i/2) *probabilityMW)  # 1.25? times your winnings 
                     - ((i + 0.25*i) *probabilitySL) # Lose 25% of your principal amount
                     - ((i*0.5 +i) *probabilityML)  # Lose 50% of your principal amount
                     - ((2*i)*probabilityBL) # Lose 100% of your principal amount
                     )/20

    # Show each column from expected value
    print(f"{'BW':<{col_width}}{'$'+str(i):<{col_width}}{probabilityBW/20:<{col_width}}{(i)*probabilityBW/20:<{col_width}}")
    print(f"{'MW':<{col_width}}{'$'+str(i/2):<{col_width}}{probabilityMW/20:<{col_width}}{(i/2)*probabilityMW/20:<{col_width}}")
    print(f"{'SL':<{col_width}}{'-$'+str(i + 0.25*i):<{col_width}}{probabilitySL/20:<{col_width}}{-(i + 0.25*i)*probabilitySL/20:<{col_width}}")
    print(f"{'ML':<{col_width}}{'-$'+str(i*0.5 +i):<{col_width}}{probabilityML/20:<{col_width}}{-(i*0.5 +i)*probabilityML/20:<{col_width}}")
    print(f"{'BL':<{col_width}}{'-$'+str(2*i):<{col_width}}{probabilityBL/20:<{col_width}}{-(2*i)*probabilityBL/20:<{col_width}}")




    print(f"Expected Value: ${expectedValue}")
    print("\n")