# 가장 가까운 같은 글자
def solution(s):
    index = {x: -1 for x in s}
    answer = []
    for i, value in enumerate(s):
        if index[value] == -1:
            answer.append(index[value])
            index[value] = i
        else:
            answer.append(i-index[value])
            index[value] = i
    return answer
