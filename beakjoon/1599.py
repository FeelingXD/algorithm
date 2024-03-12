# 민식어
"""
a b c d e f g h i j k l m n    o p q r s t u v w x y z
a b k d e   g h i     l m n ng o p   r s t u   w   y
<- 한칸씩 밀어서 단어를 변경해서 사용
"""
import sys

input = sys.stdin.readline


def minsik_word(w: str):
    # c -> k 로 변경하는경우 민식어에서 k는 c의 우선순위를 가진다.
    # ng 문자는 n -> ng -> o 의 우선순위를 가진다.
    tmp = ""
    before_n = False
    for i in range(len(w)):
        if before_n:
            before_n = False
            if w[i] == "g":  # ng 의경우
                tmp += "n"
                continue
            else:
                tmp += "m"  # 아닐경우 우선순위를 먼저 변경해준다.
        match w[i]:
            case "n":
                before_n = True
            case "k":
                tmp += "c"
            case "l":
                tmp += "j"
            case "m":
                tmp += "l"
            case wildcard:  # default 와일드카드
                tmp += wildcard
    if before_n:
        tmp += "m"
    return tmp


def solution():
    N = int(input())
    words = [input().strip() for _ in range(N)]
    words.sort(key=minsik_word)

    for word in words:
        print(word)


if __name__ == "__main__":  # 실행되는 부분
    solution()
    pass
