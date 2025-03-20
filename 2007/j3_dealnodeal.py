briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
opened = []

# total number of cases opened
n = int(input())
# making list of all opened cases
for _ in range(n):
    opened_case = int(input())-1
    opened.append(briefcases[opened_case])
# removing opened cases from the briefcase list
for case in opened:
    briefcases.remove(case)

# dealer offer input
offer = int(input())

# deal if offer is greater than the average of briefcase value else no deal
print("deal") if offer > sum(briefcases)//len(briefcases) else print("no deal")

