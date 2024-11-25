# possible combinations
# BB + BB
# Bb + BB
# BB + Bb
# Bb + Bb
# Bb + bb
# bb + Bb
# bb + bb

# as long as at least one parent gene is AA (all dominant) then the child muct have a dominant attribute
# can only guarantee that the children attribute is recessive if both parents have fully recessive genes (aa or bb)
def valid(gene1, gene2, attribute):
    if gene1[0].isupper() and gene1[1].islower() and gene2[0].isupper() and gene2[1].islower():
        return True
    if gene1.isupper() or gene2.isupper():
        if attribute.isupper():
            return True
        return False
    if gene1.islower() and gene2.islower():
        if attribute.islower():
            return True
        return False
    return True

alice = input()
bob = input()
children = int(input())
for _ in range(children):
    child = input()
    valid_child = True
    for i in range(5):
        # print(alice[i*2:i*2+2])
        # print(bob[i*2:i*2+2])
        # print(child[i])
        # print(valid(alice[i*2:i*2+2], bob[i*2:i*2+2], child[i]))
        # print()
        if not valid(alice[i*2:i*2+2], bob[i*2:i*2+2], child[i]):
            valid_child = False
    if valid_child:
        print("Possible baby.")
    else:
        print("Not their baby!")


