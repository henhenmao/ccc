

def different(a, b):
    if a.isalpha() and b.isnumeric():
        return True
    if (a == "+" or a == "-") and b.isalpha():
        return True
    if a.isnumeric() and (b == "+" or b == "-"):
        return True
    return False



instruction = input()

yeah = []

prev = "a"
for s in instruction:
    if different(s, prev):
        yeah.append("#")
    yeah.append(s)
    prev = s

yeah = ("".join(yeah)).split("#")
for i in range(0, len(yeah), 3):
    if yeah[i+1] == "+":
        tune = "tighten"
    else:
        tune = "loosen"
    print(f"{yeah[i]} {tune} {yeah[i+2]}")

