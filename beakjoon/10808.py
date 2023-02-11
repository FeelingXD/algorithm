# 알파벳 개수
import sys
input = sys.stdin.readline
arr = input().strip()
cnt = [0]*26
for i in arr:
    cnt[ord(i)-97] += 1
print(*cnt)
