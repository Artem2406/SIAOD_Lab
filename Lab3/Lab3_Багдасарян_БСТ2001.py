
def prefix(subStr):
    prefFunc = [0]*len(subStr)
    for i in range(1,len(subStr)):
        k = prefFunc[i-1]
        while k > 0 and subStr[k] != subStr[i]:
            k = prefFunc[k-1]
        if subStr[k] == subStr[i]:
            k = k + 1
        prefFunc[i] = k
    return prefFunc

def kmp_search(subStr,line,case,space):
    space = space.lower()
    case = case.lower()
    _subStr = subStr
    _line = line
    if case == "no":
        subStr = _subStr.lower()
        line = _line.lower()
    if space =="no":
        _subStr = _subStr.replace(" ","")
        _line = _line.replace(" ","")
    index = -1
    f = prefix(subStr)
    k = 0
    for i in range(len(line)):
        while k > 0 and subStr[k] != line[i]:
            k = f[k-1]
        if subStr[k] == line[i]:
            k = k + 1
        if k == len(subStr):
            index = i - len(subStr) + 1
            break
    if space =="no":
            m=0
            n=0
            spacesNumber = 0
            while m<=k+1 and n<=len(line):
                if _line[m]==line[n]:
                    m+=1
                    n+=1
                else:
                    if line[n]==" ":
                        spacesNumber +=1
                        n+=1
            return index+spacesNumber
    else:
            return index

print("Алгоритм Кнута-Морриса-Пратта")
line = input("введите строку: ")
subStr = input("выедите подстроку: ")
case = input("Case sensitivity, write Yes or No: ")
space = input("Space sensitivity, write Yes or No: ")
import timeit
startTime = timeit.default_timer()
k = kmp_search(subStr,line,case,space)
print(k)
print("Алгоритм Кнута-Морриса-Пратта длится " + str(timeit.default_timer() - startTime) + " сек")

def displacement(subStr):
    table = [len(subStr)]*256
    for i in range(len(subStr) - 1):
        table[ord(subStr[i])] = len(subStr) - 1 - i
    return table


def bm_search(subStr, line, case, space):
    space = space.lower()
    case = case.lower()
    _subStr = subStr
    _line = line
    if case == "no":
        _subStr = _subStr.lower()
        _line = _line.lower()
    if space == "no":
        _subStr = _subStr.replace(" ", "")
        _line = _line.replace(" ", "")

    table = displacement(_subStr)
    i = len(_subStr) - 1
    j = i
    k = i
    while j >= 0 and i <= len(_line) - 1:
        j = len(_subStr) - 1
        k = i
        while j >= 0 and _line[k] == _subStr[j]:
            k -= 1
            j -= 1
        i += table[ord(_line[i])]

    if k >= len(_line) - len(_subStr):
        return -1
    else:
        if space == "no":
            m = 0
            n = 0
            spacesNumber = 0
            while m <= k + 1 and n <= len(line):
                if _line[m] == line[n]:
                    m += 1
                    n += 1
                else:
                    if line[n] == " ":
                        spacesNumber += 1
                        n += 1
            return k + 1 + spacesNumber
        else:
            return k + 1

print(" ")
print(" ")
print("Упрощенный алгоритм Бойера-Мура")
line = input("введите строку: ")
subStr = input("выедите подстроку: ")
case = input("Case sensitivity, write Yes or No: ")
space = input("Space sensitivity, write Yes or No: ")
import timeit
startTime = timeit.default_timer()
k = bm_search(subStr,line,case,space)
print(k)
print("Упрощенный алгоритм Бойера-Мура длится " + str(timeit.default_timer() - startTime) + " сек")