# 영수증
import sys
amount = int(sys.stdin.readline())
sum =0
for lines in range(int(sys.stdin.readline())):
    sum += (lambda x,y: x*y)(*list(map(int, sys.stdin.readline().split())))
if(amount == sum):
    print('Yes')
else:
    print('No')