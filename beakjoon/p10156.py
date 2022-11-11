import sys
values = list(map(int,sys.stdin.readline().split()))
answer = values[0]*values[1]-values[2] if values[0]*values[1]-values[2]>=0 else 0
print(answer)