from logging import BufferingFormatter


file = open('data.txt', 'r')
lines = file.read().splitlines()
file.close()

def convertToBin():
    binaryPasses = []
    #converts the boarding passes to binary
    for boardingpass in lines:
        binarypass = boardingpass.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0")
        binaryPasses.append(binarypass)
    return binaryPasses

# the highest seat ID on a boarding pass
def highestPass():
    #sorting binary values 
    sortedBin = sorted(convertToBin())
    #returns the highest value in decimal
    return int(sortedBin[-1], 2)

#ID of your seat
def partTwo():
    #sorting the values 
    sortedBin = sorted(convertToBin())
    max= int(sortedBin[-1], 2)
    mySeat = 0
    #loops through all seats from the list
    for x in range(max):
        if x < len(sortedBin):
            temp1 = int(sortedBin[x], 2) # to dec
            temp2 = int(sortedBin[x+1], 2)
            #compares the two seat numbers
            if temp2-1 != temp1:
                mySeat = temp1+1
                break
        else:
            break
    return(mySeat)

print(highestPass())
print(partTwo())
