import re

file = open('data.txt', 'r')
data = file.read().split('\n\n')
groups1 = [line.replace('\n', '') for line in data] # part one input
groups2 = [line.replace('\n', ' ') for line in data] # part two input 
file.close()

#filters the duplicates 
def findUniqueValue(group):
    return list(dict.fromkeys(group))

#counts the people in one group
def countPeople(item):
    return len(re.split("\s", item))

def countPeopleInAllGroups():
    size = []
    for item in groups2:
        size.append(countPeople(item))
    return size

#part one
#For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
def partOne():
    sum = 0
    for group in groups1: 
        sum = sum + len(findUniqueValue(group))
    return sum

# part two 
# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
def partTwo():
    sum = 0
    groupsize = countPeopleInAllGroups()
    # find how many duplicated
    for group in groups1: 
        current = groups1.index(group)
        possibilities = ["a", "b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in range (len(possibilities)):
            found = len(re.findall(possibilities[i], group))
            if found == groupsize[current]:
                sum += 1
    return sum

print(partOne())
print(partTwo())



