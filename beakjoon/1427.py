# 소트인사이드
import sys
input = sys.stdin.readline

num = input().strip()

for i in sorted([int(i) for i in num], reverse=True):
    print(i, end='')
