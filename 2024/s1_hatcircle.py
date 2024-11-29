

n = int(input()) # numner of peopel is always even

hats = []
i = 0
j = n//2
count = 0
for _ in range(n): 
    hats.append(int(input()))

while j < n:
    if hats[i] == hats[j]:
        count += 2
    i += 1
    j += 1

print(count)