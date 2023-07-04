
from collections import deque

# 카드 뭉치


def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    cards1.append(-1)
    cards2.append(-1)
    return showdown(cards1, cards2, goal)


def showdown(cards1, cards2, goal):
    stack = []
    s = len(goal)
    for word in goal:
        if word in (cards1[0], cards2[0]):
            if word == cards1[0]:
                stack.append(cards1.popleft())
            else:
                stack.append(cards2.popleft())
        else:
            return "No"
    if goal == stack:
        return "Yes"
    else:
        return "No"
