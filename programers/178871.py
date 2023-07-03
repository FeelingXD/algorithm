# 달리기 경주
from collections import defaultdict


def solution(players, callings):
    dict_rank_name = defaultdict(lambda: "null")
    dict_name_rank = defaultdict(int)
    for i, p in enumerate(players, 1):
        dict_rank_name[i] = p
        dict_name_rank[p] = i
    for call in callings:
        swaprank(call, dict_rank_name, dict_name_rank)

    answer = []
    for i in range(len(players)):
        answer.append(dict_rank_name[i+1])
    return answer


def swaprank(player, dict_rank_name, dict_name_rank):

    tmp_rank = dict_name_rank[player]  # 변경할선수의 원래 등수
    update_rank = int(tmp_rank)-1  # 순위를 -1 시킴
    tmp_player = dict_rank_name[update_rank]  # 기존 앞질러있던선수

    dict_rank_name[tmp_rank], dict_rank_name[update_rank] = tmp_player, player
    dict_name_rank[tmp_player], dict_name_rank[player] = tmp_rank, update_rank


print("🐍 File: programers/#test.py | Line: 3",
      solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
