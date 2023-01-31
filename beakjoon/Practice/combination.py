arr = [1, 2, 3]
subset = [[]]

for num in arr:
    for y in range(len(subset)):
        subset.append(subset[y]+[num])
print(subset)
print([[sum(i), i] for i in subset])
