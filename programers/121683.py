# [PCCP 모의고사 #1] 1번 - 외톨이 알파벳
from collections import defaultdict


def solution(input_string):
    ans = ""
    dic = defaultdict(lambda: -1)
    check = defaultdict(lambda: True)
    for i, c in enumerate(input_string):
        if dic[c] == -1:  # 없을경우 최근인덱스 추가하기
            dic[c] = i
        else:
            if dic[c] == i - 1:
                dic[c] = i
            else:
                if check[c]:
                    check[c] = False
                    ans += c
    ans = "".join(sorted(list(ans)))
    return ans if ans else "N"
