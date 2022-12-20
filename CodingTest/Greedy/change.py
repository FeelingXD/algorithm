# 거스름돈
# 거스름돈 동전 종류  [500,100,50,10]

def solution(change):
    answer = []  # 동전 종류 갯수
    coin_type = [500, 100, 50, 10]

    for coin in coin_type:
        _, change = divmod(change, coin)
        answer.append(_)
    return answer


solution(1260)
print("🐍 File: Greedy/change.py | Line: 14 | undefined ~ solution(1260)", solution(1260))
