# 거짓말
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
knownlist = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knownlist:
            knownlist = knownlist.union(party)

cnt = 0
for party in parties:
    if party & knownlist:
        continue
    cnt += 1
print(cnt)
