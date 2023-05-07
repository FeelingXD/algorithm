import sys
from collections import deque
input = sys.stdin.readline

while True:
    v = input().strip()
    if v == '0':
        break
    else:
        print('yes' if v == v[::-1] else 'no')
