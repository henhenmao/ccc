
quarters = int(input())
slots = [int(input())%35, int(input())%100, int(input())%10]
curr = 0
count = 0

while quarters:
    quarters -= 1
    count += 1

    # need to put this BEFORE the calculations
    slots[curr] += 1

    if curr == 0 and slots[curr] == 35:
        quarters += 30
        slots[curr] = 0
    elif curr == 1 and slots[curr] == 100:
        quarters += 60
        slots[curr] = 0
    elif curr == 2 and slots[curr] == 10:
        quarters += 9
        slots[curr] = 0

    curr += 1
    if curr == 3:
        curr = 0

print(f"Martha plays {count} times before going broke.")
