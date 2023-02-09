# 가장 큰수
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: 3*x, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
