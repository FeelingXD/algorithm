N, M = map(int, input().split())
a = set()
b = set()
for i in range(N):
    a.add(input())
for j in range(M):
    b.add(input())
print(len(a & b))
for i in sorted(a & b):
    print(i)
