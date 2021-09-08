import re

file = open('data.txt', 'r')
bags = file.read().splitlines()
file.close()

found = 0



#original colors 
colors = ["(shiny gold bags)", "(bright white bags)","(muted yellow bags)", "(dark orange bags)", "(light red bags)"] 
colorsNum = ["\d{1,} shiny gold", "\d{1,} bright white","\d{1,} muted yellow", "\d{1,} dark orange", "\d{1,} light red"] 
values = [1,1,1,2,2]

#regex
splitWord = "(contain)"
digit = "(\d{1,})"

#loops through all the possible bag colors 
for bag in bags:
    # split to dictionarylike 
    combination = re.split(splitWord, bag)
    parent = combination[0]
    child = combination[2]

    i = 0
    #loops through all the possible bag colors 
    for color in colors: 
        # parent bag ==> 1
        if re.search(color, parent): #perfect 
            found += 1
        # child ==> digit
        if re.search(colorsNum[i], child): 
            sub = re.search(colorsNum[i], child).group()
            number = int(re.search(digit, sub).group()) # value of the bag
            found += ( int(number) * values[i]) 
            # new colors to the lists 
            colors.append(re.split("bags",parent)[0]) 
            values.append(number) 
            colorsNum.append("\d{1,} " + re.split("bags",parent)[0])
            print(child)
        i += 1

    # remove the already counted bags ??????

print(found)
