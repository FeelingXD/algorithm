# 버블 소트
import sys
input = sys.stdin.readline

c_nums = int(input())
li = []
for i in range(c_nums):
    li.append((int(input()), i))
s_li = sorted(li)

print(max([s_li[i][1]-li[i][1] for i in range(c_nums)])+1)
