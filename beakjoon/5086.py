# 배수와 약수
import sys
input = sys.stdin.readline

while case := tuple(map(int, input().split())):
    answer = 'neither'
    match case:
        case (0, 0):
            break
        case (p1, p2):
            if p1 <= p2 and p2 % p1 == 0:
                answer = 'factor'

            elif p1 % p2 == 0:
                answer = 'multiple'
    print(answer)
