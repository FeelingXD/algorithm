# 모의고사
def solution(answer):

    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    dic = {1: 0, 2: 0, 3: 0}

    dic[1] = len([v for i, v in enumerate(answer)
                 if answer[i] == answer_1[i % 5]])
    dic[2] = len([v for i, v in enumerate(answer)
                 if answer[i] == answer_2[i % len(answer_2)]])
    dic[3] = len([v for i, v in enumerate(answer)
                 if answer[i] == answer_3[i % len(answer_3)]])
    tmp_max = max(dic.values())

    answer = [k for k, v in dic.items() if v == tmp_max]

    return answer
