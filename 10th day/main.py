from collections import Counter

file = open('data.txt', 'r')
jolts = file.read().splitlines()
file.close()

jolts = [int(i) for i in jolts]

sortedAdapters = sorted(jolts)
builtInAdapter = int(max(jolts)) + 3

adapters = sorted(sortedAdapters + [0, builtInAdapter])
diff = Counter([adapters[i] - adapters[i - 1] for i in range(1, len(adapters))]) 

product = diff[1] * diff[3]

# number of 1-jolt differences multiplied by the number of 3-jolt differences
print(str(product))
