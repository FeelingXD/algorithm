import sys
input = sys.stdin.readline


n = int(input())
sum_ = 0
for i in range(1, n+1):
    sum_ += (n//i)*i

print(sum_)
