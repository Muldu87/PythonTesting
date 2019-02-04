import sys
import numbers
import re


def Convert(input):
    # find the romen number.
    if isinstance(input, numbers.Number):
        if input > 5999:
            print("Max number exceeded. Please go no further than 5999.")
        else:
            result = GetRomertal(input)
            print("%d is %s!" % (input, result))
    elif input.isalpha():
        m = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
        if m.match(input):
            result = GetNumberFromRomanNumber(input)
            print("%s is %d!" % (input, result))
        else:
            print('invalid input')
    else:
        print("invalid value")


def GetRomertal(input):
    result = (input // 1000) * 'M'
    input -= ((input // 1000) * 1000)
    if input > 899:
        result += 'CM'
        input -= 900
    else:
        result += (input // 500) * 'D'
        input -= ((input // 500) * 500)
    if input > 399:
        result += 'CD'
        input -= 400
    else:
        result += (input // 100) * 'C'
        input -= ((input // 100) * 100)
    if input > 89:
        result += 'XC'
        input -= 90
    if 39 < input < 50:
        result += 'XL'
        input -= 40
    else:
        result += (input // 50) * 'L'
        input -= ((input // 50) * 50)
    if 9 < input < 30:
        result += (input // 10) * 'X'
        input -= ((input // 10) * 10)
    if input == 9:
        result += 'IX'
        input -= 9
    if 5 < input < 9:
        calc = (input - 5) // 1 * 'I'
        num = 'V'
        result += ("%s%s" % (num, calc))
    if input == 4:
        result += 'IV'
    if 0 <= input <= 3:
        result += (input // 1) * 'I'
        input -= (input // 1)

    return result


def GetNumberFromRomanNumber(input):
    pv = ''
    result = 0
    for c in input:
        if c == 'M' and pv != 'C':
            result += 1000
        elif c == 'M' and pv == 'C':
            result += 800
        elif c == 'D' and pv != 'C':
            result += 500
        elif c == 'D' and pv == 'C':
            result += 300
        elif c == 'C' and pv != 'X':
            result += 100
        elif c == 'C' and pv == 'X':
            result += 80
        elif c == 'L' and pv != 'X':
            result += 50
        elif c == 'L' and pv == 'X':
            result += 30
        elif c == 'X' and pv != 'I':
            result += 10
        elif c == 'X' and pv == 'I':
            result += 8
        elif c == 'V' and pv != 'I':
            result += 5
        elif c == 'V' and pv == 'I':
            result += 3
        elif c == 'I':
            result += 1

        pv = c

    return result


Convert("XX")

Convert(20)
