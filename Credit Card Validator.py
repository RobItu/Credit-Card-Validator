#Validate a credit card using Luhn Algorithm
#Rules: 16 number credit card
#       Starting from the rightmost digit, double the value of every SECOND digit
#       IF doubling of a number results in a number greater than 9, add the additional digits together.
#       Sum up all of the digits (original un-doubled plus the doubled)
#       If the total number is equal to 10 then the card is VALID
CCNumber = int(input('Please input a Credit Card Number\n'))
CCNumber2=str(CCNumber)
IndexLength = int(len(CCNumber2)-2)
#=======================================================
i=0
for OddDigit in CCNumber2:
    print(OddDigit)
    length = int(len(OddDigit))
    if i==IndexLength:
        break
    elif length>1:
        print('TEST')
        break
    else:
        OddDigit = int(CCNumber2[i]) + int(CCNumber2[i])
        i+=2
#======================================================
