# 큰 수 만들기
import sys
input = sys.stdin.readline

n = input().rstrip()
li = list(map(str, input().split()))
li.sort(key=lambda x: x*3, reverse=True)
print(int(''.join(li)))
