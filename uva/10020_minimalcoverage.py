

# just one test case for now, will fix later

def minimalCoverage():
    m = int(input())

    segments = []

    while True:
        temp = [int(i) for i in input().split()]
        if temp == [0, 0]:
            break
        segments.append(temp)

    segments = [segment for segment in segments if not segment[1] < 0] # filtering out useless segments
    segments.sort(key=lambda x: (x[0], -x[1])) # earliest start with latest ends

    # if len(segments) == 0:
    #     print(0)
    #     return
    
    # print(segments)

    curr = 0
    end = 0
    count = 0

    segment_output = []

    while end < m: # stop when you pass or equal the threshold
        # loop among the segments who have starts less than current end
        temp = curr
        furthest_end = end
        furthest_segment = -1
        while temp < len(segments):
            if segments[temp][0] > end:
                break
            if segments[temp][1] > furthest_end:
                furthest_end = segments[temp][1]
                furthest_segment = segments[temp]
            temp += 1
        if furthest_segment == -1 or furthest_end <= end:
            break
        
        count += 1
        segment_output.append(furthest_segment)

        end = furthest_segment[1]

        curr += 1


    print(count)
    for s in segment_output:
        print(*s, end="")
    if n < t-1:
        print()


t = int(input())
a = input()
for n in range(t):
    minimalCoverage()
    if n < t-1:
        a = input()

    