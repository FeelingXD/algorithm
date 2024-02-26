# Z
import sys

input = sys.stdin.readline


def solution():
    n, r, c = map(int, input().split())

    def search(y, x, l, current):
        if (y, x) == (r, c):
            return current
        else:
            l //= 2
            if y + l <= r and x + l <= c:  # 목표가 4사분 면 일떄
                return search(y + l, x + l, l, current + 3 * l**2)
            elif y + l <= r:  # 목표가 3 사분면일떄
                return search(y + l, x, l, current + 2 * l**2)
            elif x + l <= c:
                return search(y, x + l, l, current + l**2)
            else:
                return search(y, x, l, current)
        pass

    pass
    print(search(0, 0, 2**n, 0))


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
