# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import decimal


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def p4():
    x = 3
    print(x)
    wenhaoyi = 123
    print(wenhaoyi)
    y = 5
    print(y)
    print(x, y)
    (x, y) = (y, x)
    print(x, y)
    print('I love China')
    print("I love China")
    print('"I love China"')
    print('\"I love China\"')


def p5():
    print("D:\three\two\one\now")
    print("D:\\three\\two\\one\\now")
    print(r"D:\three\two\one\now")
    print("abc     \n\
           123 \n\
          \n\\n\\n")
    print('''
    hello world1
    hello world2
    hello world3''')

    print(520 + 1314)
    print('520' + '1314')
    print("hello world \n" * 5)


def p6():
    temp = input("guess what number in my mind now\n")
    guess = int(temp)
    if guess == 8:
        print("that is correct")
    else:
        print("wrong number")
    print("game over")


def p7():
    count = 3
    while count > 0:
        temp = input("guess what number in my mind now\n")
        guess = int(temp)
        if guess == 8:
            print("that is correct")
            break
        else:
            if guess < 8:
                print("too small")
            else:
                print("too big")
            count = count - 1
    print("game over")


def p8():
    print(random.randint(1, 100))
    print(random.getstate())


def p9():
    print(0.1 + 0.2)
    print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))
    print(0.00005)
    x = 1 + 2j
    print(x.real)
    print(x.imag)


def p10():
    output = 3 / 2
    output = 3 // 2
    output = -3 // 2
    output = 3 % 2
    output = divmod(3, 2)
    output = divmod(-3, 2)
    output = abs(-520)
    output = abs(1 + 2j)
    output = abs(1 + 2j) * abs(1 + 2j)
    output = int("520")
    output = int(3.14)
    output = int(9.99)
    output = float("3.14")
    output = float(520)
    output = float(22.33)
    output = float(2E6)
    output = complex("1+2j")  # no space between
    output = pow(2, 3)
    output = 2 ** 4
    output = pow(2, 3, 5)
    output = 2 ** 3 % 5
    print(output)


def p11():
    output = bool(250)
    output = bool("250")
    output = bool("")
    output = bool(False)
    output = bool(0)
    print(output)


def p12():
    output = 3 and 4
    output = 0 and 4
    output = 3 or 4
    output = 0 or 4
    output = not 1 and 0 or 1
    print(output)


def p16():
    age = 5
    print("less than 18") if age < 18 else print("equal or over 18")
    a = 3
    b = 5
    if a < b:
        small = a
    else:
        small = b
    print(small)

    small = a if a < b else b
    print(small)

    score = 100
    if 0 <= score < 60:
        level = "D"
    elif 60 <= score < 80:
        level = "C"
    elif 80 <= score < 90:
        level = "B"
    elif 90 <= score < 100:
        level = "A"
    elif score == 100:
        level = "S"
    print(level)

    level = ('D' if 0 <= score < 60 else
             'C' if 60 <= score < 80 else
             'B' if 80 <= score < 90 else
             'A' if 90 <= score < 100 else
             'S')
    print(level)


def p17():
    # love = "yes"
    # while love == "yes":
    #     love = input("Do you love me today？")
    i = 1
    sum = 0
    while i <= 1000000:
        sum += i
        i += 1
    print(sum)


def p18():
    i = 1
    while i < 5:
        print("循环内，i的值是", i)
        if i == 3:
            break
        i += 1
    else:
        print("run else code")

    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(j, "*", i, "=", j * i, end=" ")
            j += 1
        print()
        i += 1


def p19():
    for each in "ABCDE":
        print(each)
    i =0
    while i <len("ABCDE"):
        print("ABCDE"[i])
        i += 1
    for i in range(11):
        print(i)

    for i in range(5,10):
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # p4()
    # p5()
    # p6()
    # p7()
    # p8()
    # p9()
    # p10()
    # p11()
    # p12()
    # p16()
    # p17()
    # p18()
    p19()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
