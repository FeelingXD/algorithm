n_li=[]
unique=[]
for i in range(10):
    n_li.append(int(input()))
for i in range(len(n_li)):
    if n_li[i]%42 not in unique:
        unique.append(n_li[i]%42)
print(unique)
print(len(unique))
