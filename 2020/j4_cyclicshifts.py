


def cyclicShifts():
    text, word = input(), input()
    isTrue = False
    for i in range(len(word)):
        for j in range(len(text)):
            temp = word[len(word)-i-1:len(word)]+word[:len(word)-i-1]
            temp2 = text[j:j+len(word)]
            if temp[0] == temp2[0] and temp == temp2:
                print("yes")
                return
    print("no")
cyclicShifts()