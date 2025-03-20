
# this solution uses a counting sort algoritm to find the longest possible length fence

# starting with your pieces of boards and their respective sizes, you find the frequency
# of each wood piece of length 1-2000 (1 < wood size < 2000). i = wood size, w[i] = frequency of wood
#
# you also create a data structure to keep track of the possible fences you can make
# of length 1-4000 (2 < possible board length < 4000). i = possible board length, fence[i] = all ways to get that length

def nailed():
    n = int(input())
    wood = [int(i) for i in input().split()]
    w = [0] * 2024 # [0,1,1,1,1]
    fence = [0] * 4050
    for i in range(len(wood)):
        w[wood[i]] += 1

    for i in range(1, len(w)): 
        if i == 0:
            continue
        for j in range(i, len(w)):
            if j == 0:
                continue
            if i == j:
                temp_length = w[i]//2 # 0
                fence[2*i] += temp_length
            else:
                temp_length = min(w[i], w[j]) # 1
                fence[i+j] += temp_length

    max_length = max(fence)
    count = 0
    for i in fence:
        if i == max_length:
            count += 1

    print(f"{max_length} {count}")
nailed()

