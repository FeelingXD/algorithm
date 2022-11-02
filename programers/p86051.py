def solution(numbers):
    return sum(set([count for count in range(10)]) -set(numbers))