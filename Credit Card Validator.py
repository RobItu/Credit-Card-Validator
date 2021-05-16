#Validate a credit card using Luhn Algorithm
#Rules: 16 number credit card
#       Starting from the rightmost digit, double the value of every SECOND digit
#       IF doubling of a number results in a number greater than 9, add the additional digits together.
#       Sum up all of the digits (original un-doubled plus the doubled)
#       If the total number is equal to 10 then the card is VALID

Counter = 1
while Counter <4:
    CCNumber = input('Please Input a 16 digit Credit Card number\n')
    CCNumber2 = str(CCNumber)
    InputLength = int(len(CCNumber2))
    IndexLength = int(len(CCNumber2) + 1)
    if CCNumber.isnumeric() and InputLength>13:

        if InputLength%2==0:
            i=0
            Total = 0
            for OddDigit in CCNumber2:
                if i==IndexLength-1:
                    break
                elif int(CCNumber2[i])>4:
                    Niners = int(CCNumber2[i]) + int(CCNumber2[i])
                    Double = str(Niners)
                    Add = int(Double[0])+int(Double[1])
                    #print(Add)
                    Total += int(Add)
                    i += 2
                else:
                    #print(CCNumber2[i])
                    Total+=int(CCNumber2[i])*2
                    i+=2
        #print('Total is '+ str(Total))
#=================================================================
        #Adding single digits
            i=1
            Total2=0
            for EvenDigits in CCNumber2:
                if i == IndexLength:
                    break
                else:
                    #print(CCNumber2[i])
                    Total2 += int(CCNumber2[i])
                    i+=2
        #print('Single Digit Total is: ' + str(Total2))
        #==================================================================
        #Adding total of Even and Odd digits
            Total3 = Total + Total2
            if Total3%10==0:
                print('Congratulations, your CC is valid!')
                break
            else:
                print('Unfortunately your CC is NOT valid')
                break
        else:
            i = 0
            Total = 0
            for OddDigit in CCNumber2:
                if i == IndexLength:
                    break
                elif int(CCNumber2[i]) > 4:
                    Niners = int(CCNumber2[i]) + int(CCNumber2[i])
                    Double = str(Niners)
                    Add = int(Double[0]) + int(Double[1])
                # print(Add)
                    Total += int(Add)
                    i += 2
                else:
                # print(CCNumber2[i])
                    Total += int(CCNumber2[i]) * 2
                    i += 2
        # print('Total is '+ str(Total))
        # =================================================================
        # Adding single digits
            i = 1
            Total2 = 0
            for EvenDigits in CCNumber2:
                if i == IndexLength-1:
                    break
                else:
                # print(CCNumber2[i])
                    Total2 += int(CCNumber2[i])
                    i += 2
        # print('Single Digit Total is: ' + str(Total2))
        # ==================================================================
        # Adding total of Even and Odd digits
            Total3 = Total + Total2
            if Total3 % 10 == 0:
                print('Congratulations, your CC is valid!')
                break
            else:
                print('Unfortunately your CC is NOT valid')
                break
    else:
        print("I'm sorry, that is not a valid input.")
        Left = 3 - Counter
        print('You have ' + str(Left) + ' attempt(s) left\n')
        Counter +=1