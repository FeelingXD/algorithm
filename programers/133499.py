# 옹알이(2)
def solution(babbling):

    babble = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for word in babbling:
        for bab in babble:
            if bab*2 not in word:
                word = word.replace(bab, ' ')
        if word.strip() == '':
            cnt += 1

    return cnt
