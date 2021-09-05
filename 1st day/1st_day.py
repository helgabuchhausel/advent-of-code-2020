file = open('1st_day.txt', 'r')
numbers = file.read().splitlines()
file.close()

sum = 2020

# the two entries that sum to 2020; what do you get if you multiply them together 
def calculation1():
    for x in numbers:
        for y in numbers:
            if sum ==int(x)+int(y):
                return int(x)*int(y)

# the product of the three entries that sum to 2020
def calculation2():
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if sum == int(x)+int(y)+int(z):
                    return int(x)*int(y)*int(z)
# part one
print(calculation1())

# part two
print(calculation2())