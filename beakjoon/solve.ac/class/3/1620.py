# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, o = map(int, input().split())
dic = {}
for i in range(1, n+1):
    dic[str(input().strip())] = i

kdic = {v: k for k, v in dic.items()}
for _ in range(o):
    tmp = str(input().strip())
    if tmp in dic.keys():
        print(dic[tmp])
    else:
        print(kdic[int(tmp)])
