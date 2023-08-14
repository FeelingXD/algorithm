# 코딩은 체육과목 입니다.
import sys
input = sys.stdin.readline

byte = int(input())

q, r = divmod(byte, 4)
prefix_long = 'long ' * q if not r else 'long ' * (q+1)
print(prefix_long+'int')
