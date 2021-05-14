#Validate a credit card using Luhn Algorithm
#Rules: 16 number credit card
#       Starting from the rightmost digit, double the value of every SECOND digit
#       IF doubling of a number results in a number greater than 9, add the additional digits together.
#       Sum up all of the digits (original un-doubled plus the doubled)
#       If the total number is equal to 10 then the card is VALID
CCNumber = int(input('Please input a Credit Card Number'))
CCNumber2=str(CCNumber)
IndexLength = int(len(CCNumber2))
i=1
for test in CCNumber2:
    print(CCNumber2[i])
    i+=2
    if i==IndexLength:
        break
Test = input('Do you want to try again')