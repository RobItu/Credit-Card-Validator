#Validate a credit card using Luhn Algorithm
#Rules: 16 number credit card
#       Starting from the rightmost digit, double the value of every SECOND digit
#       IF doubling of a number results in a number greater than 9, add the additional digits together.
#       Sum up all of the digits (original un-doubled plus the doubled)
#       If the total number is equal to 10 then the card is VALID
CCNumber = 123456798
CCNumber2=str(CCNumber)
IndexLength = int(len(CCNumber2)-1)
i=0
for test in CCNumber2:
    print(CCNumber2[i+1])
    i+=2
    if i==IndexLength:
        break