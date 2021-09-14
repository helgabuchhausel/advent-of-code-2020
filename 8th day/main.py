import re

file = open('data.txt', 'r')
originalInstructions = file.read().splitlines()
file.close()

# immediately before any instruction is executed a second time, what value is in the accumulator
def partOne():
    value = 0 
    index = 0 
    maxIndex = len(originalInstructions)
    isDone = []

    for i in range(maxIndex):
        isDone.append(False)

    while True: 
        if isDone[index] == False:
            if index <= maxIndex:
                isDone[index] = True
                #instruction splitting 
                combination = re.split(' ', originalInstructions[index])
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
    return value

def partTwo():
    maxIndex = len(originalInstructions)

    currentInstructions = originalInstructions
    for instruction in currentInstructions:
            
        #modify instructions 
        currentInstructions = originalInstructions
        #modify instructions
        combination = re.split(' ', instruction)
        operation = combination[0]
        argument = combination[1]
        if (re.search("jmp", operation)) or (re.search("nop", operation)):
            #replace jmp or nop
            if (re.search("jmp", operation)):
                instruction = "nop " + argument
            if (re.search("nop", operation)):
                instruction = "jmp " + argument

            #reset values for the while loop 
            value = 0 
            index = 0 
            isDone = []
            for i in range(maxIndex):
                isDone.append(False)

                #try the new list  
            while True: 
                if isDone[index] == False and index < maxIndex:
                    if index <= maxIndex:
                        isDone[index] = True
                        #instruction splitting 
                        combination = re.split(' ', originalInstructions[index])
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
                        break
                            

                print(value)
                print(index)

                print("TRIED")
        else:
            print("NOTHING TO CHANGE HERE")
            print(currentInstructions.index(instruction))
    



print("value: " + str(partOne()))
partTwo()