

p = "ABCDE"
while True:
  b = int(input())
  n = int(input())
  if b == 4 and n == 1:
    print(" ".join(p))
    break
  elif b == 1:
    count = 1
    while count <= n:
      p = p[1:5] + p[0]
      count += 1
  elif b == 2:
    count = 1
    while count <= n:
      p = p[4] + p[0:4]
      count += 1
  elif b == 3:
    count = 1
    while count <= n:
      p = p[1] + p[0] + p[2:5]
      count += 1