import sys
from collections import deque
input = sys.stdin.readline

li = deque()

fir = deque([i for i in list(map(str, input().split()))])
l = int(fir.popleft())
li += [int(i[::-1]) for i in fir]
while len(li) != l:
    li += [int(i[::-1])for i in list(map(str, input().split()))]

for i in sorted(li):
    print(i)
