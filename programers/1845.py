# 폰켓몬
def solution(nums):
    num_lens = len(set(nums))
    result = len(nums)//2

    return result if result < num_lens else num_lens
