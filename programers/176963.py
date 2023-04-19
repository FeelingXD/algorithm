# 추억점수
def solution(name, yearning, photo):
    scores = {i: j for i, j in zip(name, yearning)}
    answer = []
    for i in photo:
        tmp = 0
        for j in i:
            if j in scores:
                tmp += scores[j]
        answer.append(tmp)
    return answer
