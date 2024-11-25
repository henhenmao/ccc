
start_day, month_days = [int(i) for i in input().split()]

print("Sun Mon Tue Wed Thr Fri Sat")
if start_day != 7:
    space = "    " * (start_day-1) + "  1 "
else: 
    space = "    " * (start_day-1) + "  1"

day = 2
counter = start_day + 1
while day <= month_days:
    while counter <= 7:
        if day == month_days+1:
            space = space[:len(space)-1]
            break
        if len(str(day)) == 1:
            space += f"  {day}"
        else:
            space += f" {day}"
        if counter != 7:
            space += " "
        counter += 1
        day += 1
    # print(len(space))
    print(space)
    space = ""
    counter = 1
