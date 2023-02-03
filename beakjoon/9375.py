# 패션왕 신해빈
import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    dic = {}
    answer = 1
    for _ in range(int(input())):
        data = input().split()[1]
        dic[data] = dic.get(data, 0)+1

    for i in dic.keys():
        answer *= dic.get(i)+1
    print(answer-1)
