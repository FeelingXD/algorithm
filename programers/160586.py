# 대충만든 자판
from collections import defaultdict


def solution(keymap, targets):
    dic = defaultdict(int)
    answer = []

    for word in keymap:
        for i, c in enumerate(word, 1):
            if not dic[c] or i < dic[c]:
                dic[c] = i

    for target in targets:
        cnt = 0
        able = True
        for c in target:
            if not dic[c]:
                able = False
            else:
                cnt += dic[c]

        answer.append(cnt) if able else answer.append(-1)
    return answer
