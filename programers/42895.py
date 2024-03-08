# N으로 표현


def plus_case(a, b):
    return a + b


def minus_case(a, b):
    return a - b


def multiple_case(a, b):
    return a * b


def divide_case(a, b):
    return 0 if b == 0 or a // b != a / b else a // b


def solution(N, number):
    dp = [[] for _ in range(9)]  # 최대 8개
    for i in range(1, len(dp)):
        tmp_comb = set()
        tmp_comb.add(int(str(N) * i))
        for j in range(1, i):
            for v1 in dp[i - j]:  # set
                for v2 in dp[j]:  # set
                    numbers = (v1, v2)
                    tmp_comb.add(plus_case(*numbers))
                    tmp_comb.add(minus_case(*numbers))
                    tmp_comb.add(multiple_case(*numbers))
                    if div_case := divide_case(*numbers):
                        tmp_comb.add(div_case)
        if number in tmp_comb:
            return i
        dp[i] = tmp_comb
    return -1
