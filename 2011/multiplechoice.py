n = int(input())
student = []
correct = []
count = 0

for _ in range(n):
    student.append(input())
for _ in range(n):
    correct.append(input())

for i in range(n):
    if student[i] == correct[i]:
        count += 1

print(count)