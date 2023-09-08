# 별찍기 -7
import sys
input = sys.stdin.readline


def draw(n: int):
    draw_front(n)
    draw_end(n)


def draw_front(n):
    for i in range(n):
        print(f'{" "*(n-1-i)+"*"*(i)+"*"+"*"*(i)}')
    pass


def draw_end(n):
    for i in range(n-2, -1, -1):
        print(f'{" "*(n-1-i)+"*"*(i)+"*"+"*"*(i)}')
    pass


if __name__ == "__main__":
    draw(int(input()))
