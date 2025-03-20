

streams = []
n = int(input())
for _ in range(n):
    streams.append(int(input()))

while True:
    action = int(input())
    if action == 77: # end
        break
    elif action == 99: # split
        split_num = int(input())
        split_perc = int(input())
        split_item = streams[split_num-1]
        streams.insert(split_num, split_item*((100-split_perc)/100))
        streams.insert(split_num, split_item*((split_perc)/100))
        streams.pop(split_num-1)
    elif action == 88: # join
        join_num = int(input())
        streams.insert(join_num, streams[join_num-1]+streams[join_num])
        streams.pop(join_num-1)
        streams.pop(join_num)

for i in range(len(streams)):
    if i == len(streams)-1:
        print(round(streams[i]))
    else:
        print(round(streams[i]), end=" ")
