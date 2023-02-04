from functools import reduce
from math import comb, perm


def solution(N, M, K, capacity):  # n 학생, m 교실 갯수 ,k 감독관수 capacity[수용가능배열]
    capacity_sum = sum(capacity)

    student_cases = 1
    if capacity_sum == N:
        student_left = N
        for cap in capacity:
            student_cases *= comb(student_left, cap)
            student_left -= cap
    else:

        student_cases = 0
        capacity_mult = reduce(lambda x, y: x*(y+1), capacity, 1)
        start_v = 0
        tmp = 1
        tmp2 = N
        for i in range(-1, -len(capacity), -1):
            start_v += tmp*min(tmp2, capacity[i])
            tmp *= (capacity[i]+1)
            tmp2 -= min(tmp2, capacity[i])
            if tmp2 == 0:
                break

        for i in range(start_v, capacity_mult):

            caps = [0 for _ in range(M)]
            den = capacity_mult
            num = i
            for j in range(M):  # [3,3,4,4]
                den //= capacity[j] + 1
                caps[j] = num // den
                num %= den

            if sum(caps) == N:
                student_left = N
                current_cases = 1
                for cap in caps:
                    # nCr => n-[j]Cr .. .
                    current_cases *= comb(student_left, cap)
                    student_left -= cap
                student_cases += current_cases

    return student_cases * perm(K, M)


print(
    "🐍 File: review/chooseStudy.py | Line: 38 | undefined ~ solution(10, 3, 4, [3, 3, 4])", solution(10, 4, 4, [3, 3, 4, 4]))
