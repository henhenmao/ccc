

import math
while True:
    r = int(input())
    if r == 0:
        break
    count = 0
    for i in range(r): # y = √(r^2 - x^2)
        count += math.floor(math.sqrt(r*r-i*i))
    
    print(count*4+1)

