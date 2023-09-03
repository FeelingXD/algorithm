# Yonsei TOTO
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    minimums = []
    s_c, s_m = map(int, input().split())
    for _ in range(s_c):
        c_s, m_s = map(int, input().split())
        m_list = sorted(list(map(int, input().split())))
        minimums.append(m_list[c_s-m_s] if c_s >= m_s else 1)
    cnt = 0
    for m in sorted(minimums):
        if s_m-m < 0:
            break
        s_m -= m
        cnt += 1
    print(cnt)
