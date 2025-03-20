def arrangingbooks():
    b = input()
    count = 0
    mcount = b.count("M")
    beginningcountm = 0
    middlecountm = 0
    middlecountl = 0
    # b.count("L")
    for i in range(b.count("L")):
        if b[i] == "M":
            beginningcountm += 1
    for i in range(b.count("L"), len(b)):
        if b[i] == "L":
            count += 1
    for i in range(b.count("L"), b.count("L") + b.count("M")):
        if b[i] == "L":
            middlecountl += 1
        elif b[i] == "M":
            middlecountm += 1
    count += mcount - middlecountm - (min(beginningcountm, middlecountl))
    print(count)
arrangingbooks()