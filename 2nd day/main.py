import re

split = " "
split2 = "-"

file = open('data.txt', 'r')
lines = file.read().splitlines()
file.close()

def partOne():
    i = 0
    for line in lines:
        parts = re.split(split, line)

        constraints = re.split(split2, parts[0])
        letter = parts[1][:-1]
        password = parts[2]

        found = len(re.findall(letter, password))

        if found >= int(constraints[0]) and found <= int(constraints[1]):
            i=i+1
    return i

print(partOne())