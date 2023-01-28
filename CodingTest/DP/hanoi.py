def hanoi(n, start, end, by):
    if n == 1:
        print(f'{start} {end}')
        return
    else:
        hanoi(n-1, start, by, end)
        print(f'{start} {end}')
        hanoi(n-1, by, end, start)
