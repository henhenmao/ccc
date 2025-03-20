
# sort each set of dimensions for the boxes and items
# current theory is that
# all dimensions, when sorted, will line up perfectly so that
# no item dimension will be larger than its corresponding box dimension
# else the item will not be able to fit inside of the box



def fit(item_dim, box_dim):
    if item_dim[0] > box_dim[0] or item_dim[1] > box_dim[1] or item_dim[2] > box_dim[2]:
        return False
    return True

def getVolume(dimension):
    return dimension[0] * dimension[1] * dimension[2]

boxes = []
numBoxes = int(input())
for _ in range(numBoxes):
    boxes.append(sorted([int(i) for i in input().split()]))

items = []
numItems = int(input())
for _ in range(numItems):
    items.append(sorted([int(i) for i in input().split()]))

# loop through the items and
# for each item loop through the boxes
# if the dimensions do not align then item does not fit

for item_dim in items:
    best_box = 1000000001 # BOX CAN BE 1000x1000x1000!! DO 1000000001 NOT 1000000000!!!!
    does_not_fit = False
    for box_dim in boxes:
        item_volume = getVolume(item_dim)
        box_volume = getVolume(box_dim)
        if fit(item_dim, box_dim) and item_volume <= box_volume and box_volume < best_box:
            best_box = box_volume
    if best_box != 1000000001:
        print(best_box)
    else:
        print("Item does not fit.")




        
