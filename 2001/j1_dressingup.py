
h = int(input())
l = h*2
otherhalf = []

for i in range(h//2): # number of pirnt lines
    stars = i*2+1
    space = l-2*stars
    bow = ("*" * stars) + (" " * space) + ("*" * stars)
    otherhalf.append(bow)
    print(bow)

print("*" * l)

for i in range(len(otherhalf)-1, -1, -1):
    print(otherhalf[i])


