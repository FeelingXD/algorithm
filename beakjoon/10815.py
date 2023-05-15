# 숫자 카드
import sys
input = sys.stdin.readline
n = int(input())
s = set(map(int, input().split()))
k = int(input())
for i in list(map(int, input().split())):
    if i in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
