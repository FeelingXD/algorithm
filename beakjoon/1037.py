# 약수
import sys
input = sys.stdin.readline

n = int(input())
divs = list(map(int, input().split()))
divs.sort()
if len(divs) == 1:
    print(divs[0]**2)
else:
    print(divs[0]*divs[-1])
