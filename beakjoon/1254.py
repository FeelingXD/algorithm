# 팰린드롬 만들기
import sys
input = sys.stdin.readline

text = input().strip()


def len_pelindrom(text):
    for i in range(len(text)):
        if text[i:] == text[i:][::-1]:
            return len(text[i:])


pellen = len_pelindrom(text)
print(len_pelindrom(text) if pellen == len(
