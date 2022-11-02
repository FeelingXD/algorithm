a=[]
for i in range(1,10001):
    a.append(i+sum([int(j) for j in str(i)]))

for j in sorted(list(set(range(1,10001))-set(a))):
    print(j)
