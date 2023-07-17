# 숫자 짝꿍
from collections import defaultdict


def solution(X, Y):
    answer = []
    dic_x = defaultdict(int)
    dic_y = defaultdict(int)
    for v in X:
        dic_x[v] += 1
    for v in Y:
        dic_y[v] += 1
    dic = dic_x if len(dic_x) < len(dic_y) else dic_y
    s_dic = dic_x if dic == dic_y else dic_y
    for i in dic:
        for j in range(min(dic[i], s_dic[i])):
            answer.append(i)

    if answer and answer[0] == '0':
        return '0'
    return "-1" if answer == [] else ''.join(sorted(answer, key=lambda x: -int(x)))
