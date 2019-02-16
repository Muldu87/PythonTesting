import numbers
import re


def convert(i):
    # find the romen number.
    if isinstance(i, numbers.Number):
        if not 0 < i < 4000:
            print("Max or min number exceeded. Please go no further than 4000.")
        else:
            result = getromernumber(i)
            print("%d is %s!" % (i, result))
    elif i.isalpha():
        m = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
        if m.match(i):
            result = getnumberfromromannumber(i)
            print("%s is %d!" % (i, result))
        else:
            print('invalid input')
    else:
        print("invalid value")


def getromernumber(i):

    result = (i // 1000) * 'M'
    i -= ((i // 1000) * 1000)
    if i > 899:
        result += 'CM'
        i -= 900
    else:
        result += (i // 500) * 'D'
        i -= ((i // 500) * 500)
    if i > 399:
        result += 'CD'
        i -= 400
    else:
        result += (i // 100) * 'C'
        i -= ((i // 100) * 100)
    if i > 89:
        result += 'XC'
        i -= 90
    if 39 < i < 50:
        result += 'XL'
        i -= 40
    else:
        result += (i // 50) * 'L'
        i -= ((i // 50) * 50)
    if 9 < i < 40:
        result += (i // 10) * 'X'
        i -= ((i // 10) * 10)
    if i == 9:
        result += 'IX'
        i -= 9
    if i == 5:
        result += 'V'
        i -= 5
    if 5 < i < 9:
        calc = (i - 5) // 1 * 'I'
        num = 'V'
        result += ("%s%s" % (num, calc))
    if i == 4:
        result += 'IV'
    if 0 <= i <= 3:
        result += (i // 1) * 'I'
        i -= (i // 1)

    return result


def getnumberfromromannumber(i):
    pv = ''
    result = 0
    for c in i:
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


convert("V")

convert(5)

def check_val(i):
    try:
        val = int(i)
        return val
    except:
        return val


i = input("Enter some number or romannumber: ")


print(convert(check_val(i)))


#test the number converter.
def runtest():
    m = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    found = False
    for i in range(3999):
        result = getromernumber(i)
        if not m.match(result):
            print("%d input failed. Invalid result is: %s!" % (i, result))
            found = True
            break

    if not found:
        print('Test Passed')


def runtest2():
    if getromernumber(50) == 'L':
        print('test for 50 passed')
    if getromernumber(990) == 'CMXC':
        print('test for 990 passed')
    if getromernumber(1986) == 'MCMLXXXVI':
        print('test for 1986 passed')
    else:
        print('test for 1986 failed')




def runtest3():
    m = re.compile('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    found = False
    for i in range(3999):
        result = getromernumber(i)
        if m.match(result):
            if i != getnumberfromromannumber(result):
                print("%d input failed. Invalid result is: %s!" % (i, result))
                found = True
                break

    if not found:
        print('Test Passed')

def runtest4():
    if getnumberfromromannumber("V") != 5:
        print('test failed for 5')


runtest()

runtest2()

runtest3()

runtest4()

