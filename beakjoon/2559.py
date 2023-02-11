
# 수열
import sys
input = sys.stdin.readline


days, sw = map(int, input().split())
dInfo = list(map(int, input().split()))
answer = float('-inf')
result = []
result.append(sum(dInfo[:sw]))

for i in range(days-sw):
    result.append(result[i]-dInfo[i]+dInfo[sw+i])
print(max(result))
