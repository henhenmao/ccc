

cards = input()
cardslist = []

cards = cards.split("D")
cards[1] = cards[1].split("H")
cards[1][1] = cards[1][1].split("S")

cards = [cards[0][1:], cards[1][0], cards[1][1][0], cards[1][1][1]]
points = {"A":4, "K":3, "Q":2, "J":1}
suits = {0:3, 1:2, 2:1}

# print(cards)

clubs = 0
for c in cards[0]:
    if c in points:
        clubs += points[c]
if len(cards[0]) <= 2:
    clubs += suits[len(cards[0])]

diamonds = 0
for c in cards[1]:
    if c in points:
        diamonds += points[c]
if len(cards[1]) <= 2:
    diamonds += suits[len(cards[1])]

hearts = 0
for c in cards[2]:
    if c in points:
        hearts += points[c]
if len(cards[2]) <= 2:
    hearts += suits[len(cards[2])]

spades = 0
for c in cards[3]:
    if c in points:
        spades += points[c]
if len(cards[3]) <= 2:
    spades += suits[len(cards[3])]

pointlist = [clubs, diamonds, hearts, spades]
total = clubs + diamonds + hearts + spades


length = 31

print("Cards Dealt              Points")
for i in range(len(cards)):
    if i == 0:
        print("Clubs", end=" ")
        whitespace = 31-(6 + (len(cards[i])*2) + len(str(clubs)))

    elif i == 1:
        print("Diamonds", end=" ")
        whitespace = 31-(9 + (len(cards[i])*2) + len(str(diamonds)))

    elif i == 2:
        print("Hearts", end=" ")
        whitespace = 31-(7 + (len(cards[i])*2) + len(str(hearts)))

    elif i == 3:
        print("Spades", end=" ")
        whitespace = 31-(7 + (len(cards[i])*2) + len(str(diamonds)))

    for c in cards[i]:
        print(c, end=" ")

    print(" " * whitespace, end="")
    print(pointlist[i])

print(" " * (31-(6 + len(str(total)))), end="")
print(f"Total {total}")



