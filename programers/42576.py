# def solution(participant: list, completion: list):
#     part = {person: participant.count(person) for person in participant}
#     for i in completion:
#         part[i] -= 1
#     return [k for k, v in part.items() if v != 0][0]


# def solution(participant: list, completion: list):
#     part = {person: participant.count(person) for person in participant}
#     com = {person: -completion.count(person) for person in completion}

#     part = {**part, **com}
#     print("🐍 File: programers/42576.py | Line: 16 | solution ~ part",part)

from collections import Counter


def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]
