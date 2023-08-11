# 1
import sys
input = sys.stdin.readline

while True:
    try:
        case = int(input())
    except:
        break
    n, answer = 1, 1
    while n % case != 0:
        n = n % case
        n = 10*n+1
        answer += 1
    print(answer)
