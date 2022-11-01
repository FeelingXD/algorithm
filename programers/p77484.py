def solution(lottos, win_nums):

    win = {t:7-t for t in range(1,7)}; win[0]=6

    return win[len(set(lottos)&set(win_nums))+lottos.count(0)] , win[len(set(lottos)&set(win_nums))]
