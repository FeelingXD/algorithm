import sys
input=sys.stdin.readline
answer=[]
for i in range(int(input())):
    answer.append(int(input()))
for i in sorted(answer):
    print(i)