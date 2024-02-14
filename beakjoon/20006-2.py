# 랭킹전 대기열 (클래스 풀이)
import sys

input = sys.stdin.readline

START = "Started!"
WAIT = "Waiting!"


class Player:
    def __init__(self, info) -> None:
        level, name = info
        self.level = int(level)
        self.name = name
        pass

    def __str__(self) -> str:
        return f"{self.level} {self.name}"


class Room:
    def __init__(self, player: Player) -> None:
        self.room = [player]
        self.owner_level = player.level

    def add_player(self, player) -> None:
        self.room.append(player)

    def print_room(self) -> None:
        print(START if self.is_full() else WAIT)
        self.sort_room()
        for player in self.room:
            print(player)
        pass

    def sort_room(self):
        self.room.sort(key=lambda player: player.name)

    def is_full(self):
        return len(self.room) == m

    def validate_able_add(self, player: Player):
        return self.is_full() or abs(self.owner_level - player.level) > 10


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
        c_player = Player(input().split())  # 현재 플레이어 (레벨, 닉네임)
        if not rooms:  # 방이 비어 있을경우 새로만듬
            tmp_room = Room(c_player)
            rooms.append(tmp_room)
        else:
            renewal = False  # 갱신 여부를 체크
            for room in rooms:  # 방을 순회하며 적합한 방을찾음
                if room.validate_able_add(c_player):
                    continue
                else:  # 적합한 방을 찾은 경우
                    renewal = True
                    room.add_player(c_player)
                    break

            if not renewal:  # 적합한 방을 찾지 못한 경우 새로운 방을 생성함
                rooms.append(Room(c_player))

    for room in rooms:
        room.print_room()
    pass


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
