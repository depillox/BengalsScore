#Compute the score of the Bengals-Bills game
#Store the score of each team in a seperate int variable
#Use the Python random number generator to get the 2 random scores
#Assume the scores will be between 50 and 0 inclusive 
#Add logic to see who won and print the winning team name
#Add logic to simulate the coin flip and print the winning team 
#Look up the total capacity of Highmark Stadium: 71,608
#Assume a pretzel is $13.00 and 45% of the fans buy a pretzel
#Print the total gross profit to 2 decimal places

import random
bengalsScore = random.randint(0,50) #inclusive bounds
billsScore = random.randint(0,50) #inclusive bounds
print("Bengals: ", bengalsScore)
print("Bills: ", billsScore)
if bengalsScore > billsScore:
    print("Bengals Won!")
elif bengalsScore == billsScore:
    print("Tie")
else:
    print("Bills Won")
#Simulate the pre-game coin flip
coinFlipResult = random.randint(0,1)
# == is the test for equality
if coinFlipResult == 1:
    print("Bengals won the coin flip")
else:
    print("Bills won the coin flip")

totalPretzelGrossProfit = 71608 * .45 * 13.00
print("Total Pretzel Gross Profit:,", f'{totalPretzelGrossProfit:.2f}' )