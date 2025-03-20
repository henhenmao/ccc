
times = [1234, 111, 123, 135, 147, 159,
       210, 222, 234, 246, 258,
       321, 333, 345, 357,
       420, 432, 444, 456,
       531, 543, 555,
       630, 642, 654,
       741, 753,
       840, 852,
       951,
       1111]


count = 0
d = int(input())
count = len(times)*(d//720)
d %= 720

i = 0
curr_time = 1200
for minute in range(d):
    if str(curr_time)[-2:] == "59":
        if curr_time == 1259:
            curr_time = 100
        else:
            curr_time += 41
    else:
        curr_time += 1

    if curr_time == times[i]:
        # print("aaa " + str(times[i]))
        count += 1
        i += 1
        if i == len(times):
            i = 0
# print(curr_time)
print(count)