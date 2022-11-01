x=y=0
for i in range(3):
    a,b = map(int, input().split())
    x^=a
    y^=b
print(x,y)