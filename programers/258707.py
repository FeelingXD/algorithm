# n+1 카드게임
def solution(coin, cards):
    ans=0
    n=len(cards)
    idx=int(n/3)
    
    hands=set(cards[:idx])
    deck=set()
    able=True
    
    while able and idx<=n:
        able=False
        ans+=1 # 시작시 라운드 추가 
        
        # 현재 덱에 추가 (사용할 수 있으나 사용시 코인사용해야 함)
        for v in cards[idx:idx+2]:
            deck.add(v)
        for card in hands:
            # 핸드 카드로 카드 두개를 낼수있는경우
            if (n+1)-card in hands:
                # 카드 두장 제거
                hands.remove((n+1)-card)
                hands.remove(card)
                able =True
                break
        if not able and coin:
            for card in deck: # 여분 덱 순회
                if n+1-card in hands: # 핸드 카드에 짝을 이루는 카드가있다면
                    able=True
                    coin-=1
                    # 카드 두장 제거
                    hands.remove(n+1-card)
                    deck.remove(card)
                    break
                    
        if not able and coin>=2:
                # coin 을 두개쓰는경우 deck 에서 두개를 빼서사용하는경우
            for card in deck:
                if n+1-card in deck:
                    able=True
                    deck.remove(n+1-card)
                    deck.remove(card)
                    coin-=2
                    break
        idx+=2
    return ans
