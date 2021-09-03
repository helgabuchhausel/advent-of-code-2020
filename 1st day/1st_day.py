file = open('1st_day.txt', 'r')
numbers = file.read().splitlines()
file.close()

sum = 2020

def calculation1():
    for x in numbers:
        for y in numbers:
            if sum ==int(x)+int(y):
                return int(x)*int(y)

def calculation2():
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if sum == int(x)+int(y)+int(z):
                    return int(x)*int(y)*int(z)

print(calculation1())
print(calculation2())