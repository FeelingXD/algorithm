import math
a, b, c = map(int, input().split())
root = 0
if a == 0:
    root = -(c/b)
elif ((b**2-4*(a*c)) < 0):
    print("실근이 존재하지않음")
    exit
else:
    root = -b + math.sqrt(b**2-4*(a*c))
    print(root)
