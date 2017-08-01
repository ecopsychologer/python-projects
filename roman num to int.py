num = input("Enter a roman numeral or an integer: ")


def firstChar(num1):
    ch1 = num1.str(0)
    if ((ch1 == '0') | (ch1 == '1') | (ch1 == '2') | (ch1 == '3') | (ch1 == '4') | (ch1 == '5') | (ch1 == '6') | (ch1 == '7') | (ch1 == '8') | (ch1 == '9')):
        num = int(num, 10)

firstChar(num)

#if ((ch1 == '0') | (ch1 == '1') | (ch1 == '2') | (ch1 == '3') | (ch1 == '4') | (ch1 == '5') | (ch1 == '6') | (ch1 == '7') | (ch1 == '8') | (ch1 == '9')):
#    num = int(num, 10)
print(type(num))
