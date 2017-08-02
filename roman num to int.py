num = input("Enter a roman numeral or an integer: ")
ch1 = num[0]
ch1 = int(ch1)
roman1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def romify(num1):
    num2 = int(num1)
    if (int(num2) % 10) != 0:
        num2 = num2 - (num2 % 10.0)
        print(num2)
        print(num2 % 10.0)
    else:
        num2 = num2 / 10.0
    x = num2
    numeral = ""
    num1 = num1 % 10
    print(num2)
    if num2 <= 3:
        while x >= 0:
            numeral += "X"
            x = x - 1
        numeral += roman1[num1]
    if 3 < num2 <= 4:
        numeral = "XL"
        numeral += roman1[num1]
    if 4 < num2 <= 8:
        numeral = "L"
        x = x - 5
        while x >= 0:
            numeral += "X"
            x = x - 1
        num1 = num1 % 10
        numeral += roman1[num1]
    if 8 < num2 <= 9:
        numeral = "XC"
        numeral += roman1[num1]
    if 9 < num2 <= 10:
        num2 = num2 - 11
        numeral = "C" + romify(num2)
    return numeral
if int(num) > 399 | int(num) == 0:
    print("ERROR: NUMBER TOO HIGH")
if (ch1 == 0) | (ch1 == 1) | (ch1 == 2) | (ch1 == 3) | (ch1 == 4) | (ch1 == 5) | (ch1 == 6) | (ch1 == 7) | \
        (ch1 == 8) | (ch1 == 9):
    num = int(num)
    print(romify(num))
else:
    finalNum = int(num)
