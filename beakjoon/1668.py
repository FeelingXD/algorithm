# 트로피진열
import sys
input = sys.stdin.readline

num = int(input())
tropies = []

for i in range(num):
    tropies.append(int(input()))

mx = 0
cnt = 0
maximum = max(tropies)
left = 0
right = 0

for i in range(num):
    if tropies[i] > mx:
        cnt += 1
        mx = tropies[i]
        if mx == maximum:
            left = cnt
            break
mx = 0
cnt = 0
for i in range(num-1, -1, -1):
    if tropies[i] > mx:
        cnt += 1
        mx = tropies[i]
        if mx == maximum:
            right = cnt
            break

print(left)
print(right)
