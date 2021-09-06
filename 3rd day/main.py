with open("data.txt", "r") as file:
    map = list(map(str.strip, file.readlines()))
    w = len(map[0])
file.close()

tree = "#"
slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]

# counting all the trees you would encounter for the slope right 3, down 1:
def countTrees(slopeX, slopeY):
    x, trees = 0, 0
    for y in range(0, len(map), slopeY):
        if map[y][x] == tree:
            trees += 1
        x = (x + slopeX) % w
    return trees

# you multiply together the number of trees encountered on each of the listed slopes
def productOfSlopes():
    product = 0
    for slope in slopes:
        if product == 0:
            product = countTrees(slope[0],slope[1])
        else:
            product *= countTrees(slope[0],slope[1])
    return product

print(countTrees(3, 1))
print(productOfSlopes())