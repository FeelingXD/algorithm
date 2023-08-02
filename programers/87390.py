# n^2 배열자르기
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        y = i//n
        x = i % n
        answer.append(max(x, y)+1)
    return answer
