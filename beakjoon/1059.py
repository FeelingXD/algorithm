# 좋은구간
import sys
input = sys.stdin.readline

case = int(input())
li = list(map(int, input().split()))
num = int(input())
ans = 0
li.sort()

if num in li:
    print(ans)
    exit()

s = 0
e = 0
for i in li:
    if i < num:
        s = i
    elif i > num and e == 0:
        e = i

e -= 1
s += 1
ans = ((num-s)*(e-num+1)+(e-num))
print(ans)
