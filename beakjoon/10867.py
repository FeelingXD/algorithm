# 중복 빼고 정렬하기
import sys
input = sys.stdin.readline

input()
print(*sorted(list(set(list(map(int, input().split()))))))
