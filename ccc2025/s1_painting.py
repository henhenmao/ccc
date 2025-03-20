


a ,b, x, y = [int(i) for i in input().split()]

if a > x:
    maxbase = a
    minbase = x
else:
    maxbase = x
    minbase = a

if b > y:
    maxheight = b
    minheight = y
else:
    maxheight = y
    minheight = b

perimeter1 = 2*maxbase + 2*(minheight+maxheight)
perimeter2 = 2*maxheight + 2*(minbase+maxbase)

print(min(perimeter1, perimeter2))