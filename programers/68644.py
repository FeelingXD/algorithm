# 두 개 뽑아서 더하기
def solution(numbers):
    answer = set()
    for v1 in range(len(numbers)):
        for v2 in range(v1 + 1, len(numbers)):
            answer.add(numbers[v1] + numbers[v2])
    return sorted(list(answer))
