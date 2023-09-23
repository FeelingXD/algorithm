# No Brainer
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        have, need = map(int, input().split())
        print("MMM BRAINS") if have >= need else print("NO BRAINS")
