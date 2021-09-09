import re

file = open('data.txt', 'r')
instructions = file.read().splitlines()
file.close()

value = 0 
index = 0 
maxIndex = len(instructions)
isDone = []

for i in range(maxIndex):
    isDone.append(False)

while True: 
    if isDone[index] == False:
        if index <= maxIndex:
            isDone[index] = True
            #instruction splitting 
            combination = re.split(' ', instructions[index])
            operation = combination[0]
            argument = int(combination[1])
            #evaluation 
            ##accumulator
            if re.search("acc", operation):
                value = value + argument
                index+=1
            ##jump 
            if re.search("jmp", operation):
                index += argument
            ##no operation 
            if re.search("nop", operation):
                index+=1
        else:
            index = 0
    else:
        break
    
# immediately before any instruction is executed a second time, what value is in the accumulator
print("value: " + str(value))