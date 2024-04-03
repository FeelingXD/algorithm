# 잃어버린 괄호
import sys
from functools import reduce

input = sys.stdin.readline


def sum_plus_expression(expression):
    numberlst = list(map(int, expression.split("+")))  # + 로 분할
    return sum(numberlst)


def solution():
    expression = input().strip()
    expression_lst = expression.split("-")  # - 로 분할
    expression_lst[0] = int(sum_plus_expression(expression_lst[0]))
    expression_lst[1:] = list(map(sum_plus_expression, expression_lst[1:]))
    print(reduce(lambda a, b: a - b, expression_lst[1:], expression_lst[0]))
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
