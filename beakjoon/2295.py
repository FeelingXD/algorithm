# 세수의 합
import sys
input = sys.stdin.readline

li = set()
ans = set()
for i in range(int(input())):
    li.add(int(input()))
sums = set()
for i in li:
    for j in li:
        sums.add(i+j)

for i in li:
    for j in li:
        if (i-j) in sums:
            ans.add(i)
print(max(ans))
