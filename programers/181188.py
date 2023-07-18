# 요격 시스템
def solution(targets):
    targets.sort(key=lambda x: [x[1], x[0]])
    s = e = 0
    answer = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
    return answer
