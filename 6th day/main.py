file = open('data.txt', 'r')
data = file.read().split('\n\n')
data = [line.replace('\n', '') for line in data]
file.close()

#part one
sum = 0
for d in data: 
    #filters the duplicates 
    d = list(dict.fromkeys(d))
    #add to sum 
    sum = sum + len(d)

print(sum)
