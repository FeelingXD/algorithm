# 대표값 2
import sys
input = sys.stdin.readline

tmp = []

for _ in range(5):
    tmp.append(int(input()))
print(sum(tmp)//5)
print(sorted(tmp)[2])
