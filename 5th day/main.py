file = open('data.txt', 'r')
lines = file.read().splitlines()
file.close()

binaryPasses = []
#converts the boarding passes to binary
for boardingpass in lines:
    binarypass = boardingpass.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0") # replaced to look like binary 
    binaryPasses.append(binarypass)

#sorting the values 
sortedBin = sorted(binaryPasses)

#returns the highest value 
max = sortedBin[-1]

a = int(max, 2) # converts it to decimal value
print(a)

