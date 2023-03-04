# 명령 프롬프트
import sys

input = sys.stdin.readline

case = int(input())


answer = input().strip()
if case == 1:
    print(answer)
    exit()
for i in range(1, case):
    tmp = input().strip()
    tw = ''
    for j in range(len(tmp)):
        if tmp[j] != answer[j]:
            tw += '?'
        else:
            tw += tmp[j]
    answer = tw
print(answer)
