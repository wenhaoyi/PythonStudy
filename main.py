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
    #     love = input("Do you love me today???")
    i = 1
    sum = 0
    while i <= 1000000:
        sum += i
        i += 1
    print(sum)


def p18():
    i = 1
    while i < 5:
        print("????????????i?????????", i)
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
    i = 0
    while i < len("ABCDE"):
        print("ABCDE"[i])
        i += 1
    for i in range(11):
        print(i)

    for i in range(5, 10):
        print(i)


def p20():
    rhyme = [1, 2, 3, 4, 5, "whatever"]
    print(rhyme)
    for each in rhyme:
        print(each)
    i = 0
    while i < len(rhyme):
        print(rhyme[i])
        i += 1
    print(rhyme[-1])
    print(rhyme[1:3])
    print(rhyme[:4])
    print(rhyme[4:])
    print(rhyme[:])
    print(rhyme[0:6:2])
    print(rhyme[::-2])
    print(rhyme[::-1])


def p21():
    heros = ["?????????", "?????????"]
    heros.append("?????????")
    print(heros)
    heros.extend(["??????", "??????", "??????"])
    print(heros)
    s = [1, 2, 3, 4, 5]
    s[len(s):] = [6]
    print(s)
    s = [1, 3, 4, 5]
    s.insert(1, 2)
    print(s)
    heros.remove("??????")
    print(heros)
    heros.pop(2)
    print(heros)
    heros.clear()
    print(heros)


def p22():
    heros = ["?????????", "?????????", "?????????", "??????", "??????", "??????"]
    print(heros)
    heros[4] = "?????????"
    print(heros)
    heros[3:] = ["aaa", "bbb"]
    print(heros)
    nums = [3, 1, 9, 6, 8, 3, 5, 3]
    nums.sort()
    print(nums)
    nums.reverse()
    print(nums)
    heros.reverse()
    print(heros)
    nums = [3, 1, 9, 6, 8, 3, 5, 3]
    nums.sort(reverse=True)
    print(nums)
    print(nums.count(3))
    heros = ["?????????", "?????????", "?????????", "??????", "??????", "??????"]
    print(heros.index("?????????"))
    heros[heros.index("?????????")] = "????????????"
    print(heros)
    nums = [3, 1, 9, 6, 8, 3, 5, 3]
    print(nums.index(3, 1, 7))  # find 3 from index 1 to index 7
    nums_copy = nums.copy()
    print(nums_copy)
    nums_copy2 = nums[:]
    print(nums_copy2)


def p23():
    s = [1, 2, 3]
    t = [4, 5, 6]
    print(s + t)
    print(s * 3)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    for i in matrix:
        for each in i:
            print(each)
    for i in matrix:
        print(i)
    for i in matrix:
        for each in i:
            print(each, end=" ")
        print()
    print(matrix[2][2])
    A = [0] * 3
    print(A)
    for i in range(3):
        A[i] = [0] * 3
    print(A)
    B = [[0] * 3] * 3
    print(B)
    A[1][1] = 3
    B[1][1] = 3
    print(A)
    print(B)
    x = "ABC"
    y = "ABC"
    print(x is y)
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x is y)


def p24():
    x = [1, 2, 3]
    y = x
    x[1] = 1
    print(x)
    print(y)
    x = [1, 2, 3]
    y = x.copy()
    x[1] = 1
    print(x)
    print(y)
    x = [1, 2, 3]
    y = x[:]
    print(x)
    print(y)
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = x.copy()
    print(y)
    x[1][1] = 0
    print(x)
    print(y)
    import copy
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = copy.copy(x)
    x[1][1] = 222
    print(x)
    print(y)
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    y = copy.deepcopy(x)
    x[1][1] = 333
    print(x)
    print(y)


def p25():
    oho = [1, 2, 3, 4, 5]
    for i in range(len(oho)):
        oho[i] = oho[i] * 2
    print(oho)
    oho = [i * 2 for i in oho]
    print(oho)
    x = [i for i in range(10)]
    print(x)
    x = [i + 1 for i in range(10)]
    print(x)
    x = []
    for i in range(10):
        x.append(i + 2)
    print(x)
    y = [c * 2 for c in "whatever"]
    print(y)
    code = [ord(c) for c in "FishC"]
    print(code)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    col2 = [row[1] for row in matrix]
    print(col2)
    diag = [matrix[i][i] for i in range(len(matrix))]
    print(diag)
    diag2 = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]
    print(diag2)


def p26():
    S = [[0] * 3 for i in range(3)]
    print(S)
    S[1][1] = 1
    print(S)
    even = [i for i in range(10) if i % 2 == 0]
    print(even)
    even = [i + 1 for i in range(10) if i % 2 == 0]
    print(even)
    words = ["Great", "FishC", "Brilliant", "Excellent", "Fantastic"]
    fwords = [i for i in words if i[0] == "F"]
    print(fwords)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flatten = [col for row in matrix for col in row]
    print(flatten)
    temp = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
    print(temp)


def p27():
    rhyme = (1, 2, 3, 4, "whatever")
    print(rhyme)
    rhyme = 1, 2, 3, 4, "abc"
    print(rhyme)
    rhyme2 = rhyme[:]
    print(rhyme2)
    rhyme2 = rhyme[::-1]
    print(rhyme2)
    nums = (1, 2, 3, 4, 5, 1, 2, 3, 1)
    print(nums.count(2))
    print(nums.index(5))
    s = (1, 2, 3)
    t = (4, 5, 6)
    w = s + t
    print(w)
    for each in w:
        print(each)
    s = (1, 2, 3)
    t = (4, 5, 6)
    w = s, t
    print(w)

    t = (123, "whatever", 3.14)
    print(t)
    x, y, z = t
    print(x)
    print(y)
    print(z)


def p28():
    x = "123456"
    output = "????????????" if x == x[::-1] else "???????????????"
    print(output)
    x = "I love China"
    print(x.capitalize())
    print(x.casefold())
    print(x.title())
    print(x.swapcase())
    print(x.upper())
    print(x.lower())

    x = "whatever,abcd,12,34,56,78,90"
    print(x.center(50))
    print(x.ljust(40))
    print(x.rjust(40))
    print(x.zfill(50))
    print(x.center(40, "a"))


def p29():
    x = "ABCDEFGABC"
    print(x.count("B"))
    print(x.find("B"))
    print(x.rfind("B"))
    print(x.find("H"))
    # print(x.index("H"))
    code = """
            whatever lines
    dfsg"""
    new_code = code.expandtabs(4)
    print(new_code)
    x = "ABCDEF"
    print(x.replace("AB", "PPP"))
    table = str.maketrans("ABCDE", "12345")
    print("AB00000000".translate(table))


def p30():
    x = "I love python"
    print(x.startswith("I"))
    print(x.endswith("python"))
    print(x.endswith("py"))
    print(x.startswith("I", 1))
    print(x.startswith(" ", 1))
    print(x.endswith("py", 0, 9))
    if x.startswith(("A", "B", "I")):
        print("includes")
    x = "I love python"
    print(x.istitle())
    print(x.isupper())
    print(x.upper().isupper())
    print(x.isalpha())
    x = "abcd"
    print(x.isalpha())
    x = "i love python \n"
    print(x.isprintable())
    x = "123456"
    print(x.isdecimal())
    print(x.isdigit())
    print(x.isnumeric())
    x = "?????????"
    print(x.isdecimal())
    print(x.isdigit())
    print(x.isnumeric())
    # isalnum is like isalpha or isdecimal or isdigital or isnumeric
    x = "i love python"
    print(x.isidentifier())
    x = "i_love_python"
    print(x.isidentifier())
    x = "123i_love_python"
    print(x.isidentifier())


def p31():
    x = "    no space on left    "
    print(x.lstrip())
    x = "    no space on right    "
    print(x.rstrip())
    x = "    no space on both sides    "
    print(x.strip())

    x = "www.ilovefishc.com"
    print(x.lstrip("wcom."))  # delete until the first not the deleted one
    x = "www.ilovefishc.com"
    print(x.rstrip("wcom."))
    x = "www.ilovefishc.com"
    print(x.strip("wcom."))
    # x = "www.ilovefishc.com"
    # print(x.removeprefix())
    # x = "www.ilovefishc.com"
    # print(x.removesuffix("wcom."))
    x = "www.ilovefishc.com"
    print(x.partition("."))
    x = "www.ilovefishc.com"
    print(x.rpartition("."))
    x = "ABC,DEF,GHI"
    print(x.split())
    x = "ABC,DEF,GHI"
    print(x.split(','))
    x = "ABC,DEF,GHI"
    print(x.split(',', 1))
    x = "ABC,DEF,GHI"
    print(x.rsplit(',', 1))
    x = "ABC\nDEF\nGHI"
    print(x.split('\n'))
    x = "ABC\nDEF\nGHI"
    print(x.splitlines())
    x = "."
    print(x.join(["a", "b", "c"]))


def p32():
    year = 2021
    x = "ABCD {} jkl".format(year)
    print(x)
    a = "111"
    b = "222"
    c = "333"
    x = "a{}b{}c{}".format(a, b, c)
    print(x)
    a = "111"
    b = "222"
    c = "333"
    x = "a{2}b{1}c{0}".format(a, b, c)
    print(x)
    a = "111"
    b = "222"
    c = "333"
    x = "a{name1}b{name2}c{name3}".format(name1=a, name2=b, name3=c)
    print(x)
    x = "{:^10}"
    print(x.format(250))
    x = "{1:>10}{0:<10}"
    print(x.format(520, 250))
    x = "{left:>10}{right:<10}"
    print(x.format(right=520, left=250))
    x = "{:010}"
    print(x.format(250))
    x = "{1:$>10}{0:%<10}"
    print(x.format(520, 250))


def p33():
    print("{:+} {:-}".format(520, -520))
    print("{:,}".format(123456))
    print("{:_}".format(1234))
    print("{:.2f}".format(3.1415926))
    print("{:.2g}".format(3.1415926))
    print("{:.6}".format("I love python"))
    print("{:b}".format(80))
    print("{:c}".format(80))
    print("{:d}".format(80))
    print("{:o}".format(80))
    print("{:x}".format(80))
    print("{:#b}".format(80))
    print("{:#d}".format(80))
    print("{:#o}".format(80))
    print("{:#x}".format(80))
    print("{:e}".format(3.1415))
    print("{:E}".format(3.1415))
    print("{:f}".format(3.1415))
    print("{:F}".format(3.1415))
    print("{:G}".format(123456789))
    print("{:G}".format(3.1415))
    print("{:%}".format(3.1415))
    print("{:.2%}".format(3.1415))
    print("{:.{prec}%}".format(3.1415, prec=3))
    a = "111"
    b = "222"
    c = "333"
    x = f"a{a}b{b}c{c}"
    print(x)
    print(f"{3.1415:.2%}")
    fill = "+"
    align = "^"
    width = 10
    prec = 3
    ty = "g"
    print(f"{3.1415:{fill}{align}{width}.{prec}{ty}}")


def p34():
    s = [1, 2, 3]
    print(id(s))
    s *= 2
    print(s)
    print(id(s))
    t = (1, 2, 3)
    print(id(t))
    t *= 2
    print(t)
    print(id(t))
    x = "abc"
    y = "abc"
    print(x is y)
    x = [1, 2, 3]
    y = [1, 2, 3]
    print(x is y)
    print("a" in "abc")
    print("d" in "abc")
    print("a" not in "abc")
    print("d" not in "abc")
    x = [1, 2, 3, 4, 5]
    del x[1:4]  # delete 2,3,4 idnex
    print(x)


def p35():
    x = list("ABCDE")
    print(x)
    x = list((1, 2, 3, 4, 5))
    print(x)
    x = tuple("ABCDE")
    print(x)
    x = str([1, 2, 3, 4, 5])
    print(x)
    print(max("abcA", default="nothing"))
    print(2 ** 3)
    s = [1, 2, 3, 4, 5]
    print(sum(s))
    # print(sum(s, start=100))
    s = [1, 2, 5, 6, 8, 3, 2, 5]
    print(sorted(s))
    print(s)
    print(s.sort())  # ???
    print(s)
    t = ["sda", "bfdg", "jdfg", "d", "r", "efd"]
    print(sorted(t))
    # print(sorted(t, key=len()))
    t = "abkdsfkbsjd"
    print(sorted(t))
    print(list(reversed(t)))


def p36():
    x = [1, 1, 0]
    y = [1, 1, 9]
    print(all(x))
    print(all(y))
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    print(list(enumerate(seasons)))
    print(list(enumerate(seasons, 10)))
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))
    z = [7, 8, 9]
    zipped = zip(x, y, z)
    print(list(zipped))
    mapped = map(ord, "FishC")
    print(list(mapped))
    mapped = map(pow, [2, 3, 10], [5, 2, 3])
    print(list(mapped))
    print(list(filter(str.islower, "FishC")))
    mapped = map(ord, "FishC")
    for each in mapped:
        print(each)
    print(list(mapped))
    x = [1, 2, 3, 4, 5]
    y = iter(x)
    print(type(x))
    print(type(y))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))
    print(next(y, "nothing left"))


def p38():
    x = {"A", "B"}
    print(type(x))
    y = {"A": "value of A", "B": "value of B"}
    print(type(y))
    print(y["A"])
    b = dict(A="value1", B="value2")
    print(b["B"])
    c = dict([("A", "valueA"), ("B", "valueB")])
    print(b["B"])
    d = dict.fromkeys("FishC", 250)
    print(d)
    d.pop("s")
    print(d)
    d.pop("whatever", "there is no this key")
    del d["i"]
    print(d)
    d.clear
    print(d)


def p39():
    d = dict.fromkeys("FishC", 250)
    print(d)
    d["s"] = 666
    print(d)
    d.update(F="111", i="222")
    print(d)
    print(d.get("c", "there is no c"))
    d.setdefault("c", "code")  # if there is c, then update, is there is no c , then add the key and value
    d = dict.fromkeys("FishC", 250)
    keys = d.keys()
    values = d.values()
    items = d.items()
    print(keys)
    print(values)
    print(items)
    print(list(d))
    d = dict.fromkeys("FishC", 250)
    b = {v: k for k, v in d.items()}
    print(b)


def p40():
    s = set("FishC")
    print(s)#not in order, so index is not working but in , not in is ok
    s = set([1,1,2,3,2,3])
    print(s)
    print(len(s))
    # s.isdisjoint()
    # s.issubset()
    # s.issuperset()
    # s.union()
    # s.intersection()
    # s.difference()
    # s.symmetric_difference()


def p41():
    t = frozenset("FishC")
    print(t)
    s = set("Fish")
    print(s)
    s.update([1,1],"23")# it is like ???1123??? or [1,1,2,3]
    print(s)
    # t is not able to make this kind of changes
    s.add("45")#45 is a package not 4 and 5
    print(s)
    print(hash(1))
    print(hash(1.0))#not changeable item can be hash
    print(hash("FishC"))


def p42():
    pass


def p43(a,*,b,c):
    #/ and * show differnt type of input parameters




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p42()
    # p41()
    # p40()
    # p39()
    # p38()
    # p36()
    # p35()
    # p34()
    # p33()
    # p32()
    # p31()
    # p30()
    # p29()
    # p22()
    # p21()
    # p20()
    # p28()
    # p27()
    # p26()
    # p25()
    # p24()
    # p23()
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
    # p19()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
