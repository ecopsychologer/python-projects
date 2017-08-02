num = input("Enter a roman numeral or an integer: ")
if num.isdigit():
    ch1 = int(num[0])
roman1 = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]


def romify1(num1):
    return roman1[num1]


def romify10(num1):
    num2 = int(num1)
    numeral = ""
    num1 = num1 % 10
    num2 = num2 / 10
    num2 = int(num2)
    if num2 < 4:
        while num2 > 0:
            numeral += "X"
            num2 = num2 - 1
    if 4 <= num2 < 5:
        numeral = "XL"
    if 5 <= num2 < 9:
        numeral = "L"
        num2 = num2 - 5
        while num2 > 0:
            numeral += "X"
            num2 = num2 - 1
        num1 = num1 % 10
    if 9 <= num2 < 10:
        numeral = "XC"
    return numeral + romify1(num1)


def romify100(num1):
    num2 = int(num1)
    numeral = ""
    num1 = num1 % 100
    num2 = num2 / 100
    num2 = int(num2)
    if num2 < 4:
        while num2 > 0:
            numeral += "C"
            num2 = num2 - 1
    if 4 <= num2 < 5:
        numeral = "CD"
    if 5 <= num2 < 9:
        numeral = "D"
        num2 = num2 - 5
        while num2 > 0:
            numeral += "C"
            num2 = num2 - 1
        num1 = num1 % 10
    if 9 <= num2 < 10:
        numeral = "CM"
    return numeral + romify10(num1)


def romify1000(num1):
    num2 = int(num1)
    numeral = ""
    num1 = num1 % 1000
    num2 = num2 / 1000
    num2 = int(num2)
    if num2 <= 4:
        while num2 > 0:
            numeral += "M"
            num2 = num2 - 1
    return numeral + romify100(num1)


def intify(rom1):
    rom1 = rom1.upper()
    num1 = 0
    while num1 < 5000:
        rom2 = romify1000(num1)
        print(rom2 + " ?= " + rom1)
        if rom1 == rom2:
            print(rom2 + " = " + rom1)
            break
        else:
            num1 += 1
            print(num1)
    return num1

if num.isdigit():
    if int(num) > 4999:
        print("ERROR: INPUT NUMBER INVALID")
        print("Roman Numerals have a maximum value of 4999")
    else:
        num = int(num)
        print(romify1000(num))
elif num.isalpha():
    finalnum = intify(num)
    if int(finalnum) > 4999:
        print("ERROR: SYNTAX INVALID")
        print("Your input would be equivalent to " + str(finalnum))
    else:
        print(finalnum)
else:
    print("ERROR: INPUT INVALID")
