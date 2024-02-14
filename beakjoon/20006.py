# 랭킹전 대기열
import sys

input = sys.stdin.readline

START = "Started!"
WAIT = "Waiting!"


def print_rooms(rooms):
    """
    방을 순회하며 출력
    플레이어 인원은 닉네임이 사전순으로 앞서는 플레이어를 출력해야함
    """
    for room in rooms:
        room.sort(key=lambda x: x[1])
        print(START if len(room) >= m else WAIT)
        for player in room:
            print(*player)


def solution():
    global m
    p, m = map(int, input().split())  # 플레이어수 , 방의 최대 인원
    rooms = []
    for _ in range(p):
        c_player = list(input().split())  # 현재 플레이어 (레벨, 닉네임)
        if not rooms:  # 방이 비어 있을경우 새로만듬
            tmp_room = []
            tmp_room.append(c_player)
            rooms.append(tmp_room)
        else:
            renewal = False  # 갱신 여부를 체크
            for i, room in enumerate(rooms):  # 방을 순회하며 적합한 방을찾음
                """
                적합한 방을 찾는 조건
                1. 생성자의 레벨과 10 이상 차이가 날수 없음
                2. 방 최대인원을 초과 할 수 없음
                """
                if (
                    len(room) >= m or abs(int(c_player[0]) - int(room[0][0])) > 10
                ):  # 방 인원수 초과 하거나 생성자 레벨과의 차이가 10보다 클경우
                    continue
                else:  # 적합한 방을 찾은 경우
                    renewal = True
                    tmp_room = room + [c_player]
                    rooms[i] = tmp_room
                    break
            if not renewal:  # 적합한 방을 찾지 못한 경우 새로운 방을 생성함
                tmp_room = [c_player]
                rooms.append(tmp_room)
    print_rooms(rooms)
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
