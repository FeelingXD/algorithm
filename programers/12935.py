#제일 작은수 제거
def solution(arr):
    arr.remove(min(arr))
    return arr if arr!=[] else [-1]