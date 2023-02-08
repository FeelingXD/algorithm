# 좌표 압축
import sys
input = sys.stdin.readline
cnt = 0
dic = {}
case = int(input())
li = list(map(int, input().split()))

for i in sorted(li):
    if dic.get(i, -1) == -1:
        dic[i] = cnt
        cnt += 1
for i in range(len(li)):
    if i != len(li)-1:
        print(dic[li[i]], end=" ")
    else:
        print(dic[li[i]])
