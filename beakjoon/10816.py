# 숫자 카드 2
import sys

input = sys.stdin.readline
dic = {}
case = int(input())
cards = list(map(int, input().split()))

for card in cards:
    dic[card] = dic.get(card, 0)+1
find = int(input())
fl = list(map(int, input().split()))
for card in fl:
    if card != fl[-1]:
        print(dic.get(card, 0), end=' ')
    else:
        print(dic.get(card, 0))
