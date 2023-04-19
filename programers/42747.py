# H-index
def solution(citations):
    answer = 0
    citations.sort()

    thesis = len(citations)
    for i in range(thesis):
        if citations[i] >= len(citations) - i:
            answer += 1
    return answer
