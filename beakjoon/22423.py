# 괄호의 값 비교
import sys

input = sys.stdin.readline


def cal_bracket_score(word: str):
    left = 0
    k_l = [0] * (m + 1)
    for i in range(len(word)):  # 첫글자는 ( 이 므로 패스
        if word[i] == "(":
            left += 1
        else:
            left -= 1
            if word[i - 1] == "(":
                k_l[left] += 1
    for i in range(len(k_l) - 1):
        k_l[i + 1] += k_l[i] // 2
        k_l[i] %= 2
    return k_l


def solution():
    global m
    for _ in range(case := int(input())):
        word_a = input().strip()
        word_b = input().strip()
        m = max(len(word_a), len(word_b))

        a = cal_bracket_score(word_a)
        b = cal_bracket_score(word_b)
        breakable = False
        for i in range(m - 1, -1, -1):
            if a[i] < b[i]:
                breakable = True
                print("<")
                break
            elif a[i] > b[i]:
                breakable = True
                print(">")
                break
        if not breakable:
            print("=")

    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
