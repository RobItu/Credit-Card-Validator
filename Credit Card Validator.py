#Validate a credit card using Luhn Algorithm
#Rules: 16 number credit card
#       Starting from the rightmost digit, double the value of every SECOND digit
#       IF doubling of a number results in a number greater than 9, add the additional digits together.
#       Sum up all of the digits (original un-doubled plus the doubled)
#       If the total number is equal to 10 then the card is VALID
CCNumber = 80584556
CCNumber2=str(CCNumber)
IndexLength = int(len(CCNumber2)-2)
#=======================================================
i=0
for OddDigit in CCNumber2:
    if i==IndexLength:
        break
    elif int(CCNumber2[i])>4:
        Niners = int(CCNumber2[i]) + int(CCNumber2[i])
        Double = str(Niners)
        Add = int(Double[0])+int(Double[1])
        print(Add)
        i += 2
    else:
        print(CCNumber2[i])
        i+=2