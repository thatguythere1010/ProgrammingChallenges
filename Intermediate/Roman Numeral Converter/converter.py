inputVar = raw_input("Input: ")
inputVar = list(inputVar)
list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
numList = [1000, 500, 100, 50, 10, 5, 1]
result = 0
bracketNum = 0
brackets = []
outstandingBrackets = 0

for i in range(1,len(inputVar)+1):
    i -= 1
    if (inputVar[i] == "("):
        outstandingBrackets += 1
    elif (inputVar[i] == ")"):
        outstandingBrackets -= 1
        bracketNum += 1
    elif (any(inputVar[i] in s for s in list)):
        if (outstandingBrackets == 0):
            if (i == 0):
                for j in range(1,len(list)+1):
                    j -= 1
                    if (inputVar[i] == list[j]):
                        result += numList[j]
            else:
                var1 = 0
                var2 = 0
                for j in range(1,len(list)+1):
                    j -= 1
                    if (inputVar[i-1] == list[j]):
                        var1 = numList[j]
                for j in range(1,len(list)+1):
                    j -= 1
                    if (inputVar[i] == list[j]):
                        var2 = numList[j]
                if (var1 < var2):
                    var2 = (var2-var1)-var1
                    result += var2
                elif (var1 >= var2):
                    result += var2
        else:
            var1 = 0
            var2 = 0
            for j in range(1,len(list)+1):
                j -= 1
                if (inputVar[i-1] == list[j]):
                    var1 = numList[j]
            for j in range(1,len(list)+1):
                j -= 1
                if (inputVar[i] == list[j]):
                    var2 = numList[j]
            if (var1 < var2):
                var2 = (var2-var1)-var1
                if ((len(brackets) - 1) == bracketNum):
                    brackets[bracketNum] += var2
                else:
                    brackets.insert(bracketNum, var2)
            elif (var1 >= var2):
                if ((len(brackets) - 1) == bracketNum):
                    brackets[bracketNum] += var2
                else:
                    brackets.insert(bracketNum, var2)
    else:
        print("Character ", inputVar[i], " is not a roman numeral!")

for i in brackets:
    if (i == 1):
        print("Cannot have (I)!")
    i *= (1000 ** (len(brackets) - (brackets.index(i) + 1) + 1))
    result += i
    print(i)
print("Result: " + str(result))