# 명예의 전당


def solution(k: int, score: list):
    answer = []
    win_scores = []
    for i in range(len(score)):
        win_scores.append(score[i])
        win_scores.sort(reverse=True)
        if len(win_scores) > k:
            del win_scores[k]
        answer.append(win_scores[len(win_scores)-1])
    return answer
