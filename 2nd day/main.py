import re

split, split2 = " ", "-"

file = open('data.txt', 'r')
lines = file.read().splitlines()
file.close()

class Object:
    def __init__(self, line):
        self.line = line
        self.parts = re.split(split, line)
        self.constraints = re.split(split2, self.parts[0])
        self.letter = self.parts[1][:-1]
        self.password = self.parts[2]
        self.min =int(self.constraints[0])
        self.max = int(self.constraints[1])
        self.found = 0
    
    def find(self):
        return len(re.findall(self.letter,  self.password))

    def checkCorporatePassword(self):
        if self.find() >= self.min and self.find() <= self.max:
            return True
    
    def createIndexes(self):
        self.index1 = self.min -1 
        self.index2 = self.max -1 

    def checkPassword(self):
        self.createIndexes()
        if self.password[self.index1] == self.letter or self.password[self.index2] == self.letter :
            if not(self.password[self.index1] == self.letter and self.password[self.index2] == self.letter)  :
                return True
    
    
def partOne():
    i = 0
    for line in lines:
        currentLine = Object(line)

        if currentLine.checkCorporatePassword():
            i=i+1
    return i


def partTwo():
    i = 0
    for line in lines:
        currentLine = Object(line)

        if currentLine.checkPassword():
            i=i+1
    return(i)

print(partOne())
print(partTwo())
