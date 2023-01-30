# 설탕
import sys
input = sys.stdin.readline

sugar = int(input())
cnt = 0

while 3 <= sugar:
    if sugar % 5 == 0:
        cnt += int(sugar/5)
        sugar %= 5
        break
    else:
        sugar -= 3
        cnt += 1
print(cnt if sugar == 0 else -1)
