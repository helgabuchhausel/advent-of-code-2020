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

        min =int(constraints[0])
        max = int(constraints[1])
        found = len(re.findall(letter, password))

        if found >= min and found <= max:
            i=i+1
    return i

i = 0
for line in lines:
    parts = re.split(split, line)

    constraints = re.split(split2, parts[0])
    letter = parts[1][:-1]
    password = parts[2]
    min =int(constraints[0])
    max = int(constraints[1])

    if password[min-1] == letter or password[max-1] == letter :
        if not(password[min-1] == letter and password[max-1] == letter)  :
            i=i+1


print(partOne())
print(i)
