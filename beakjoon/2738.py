# 행렬덧셈
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li1 = []
li2 = []
result = []
for i in range(n):
    li1.append(list(map(int, input().split())))
for i in range(n):
    li2.append(list(map(int, input().split())))
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(li1[i][j]+li2[i][j])
    result.append(tmp)
for i in result:
    print(*i)
