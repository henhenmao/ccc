

cities = []

while True:
    cities.append(input().split())
    if cities[-1][0] == "Waterloo":
        break


min_city = min(cities, key=lambda n: int(n[1]))

print(min_city[0])