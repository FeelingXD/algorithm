# 별찍기 2
import sys
case = int(sys.stdin.readline())

for i in range(1,case+1):
    for k in range(case-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
