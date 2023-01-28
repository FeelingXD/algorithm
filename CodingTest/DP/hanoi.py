def hanoi(n, start, by, end):
    if (n == 1):
        print(f'원반 1 to {end}')
    else:
        hanoi(n-1, start, end, by)
        print(f'원반 {n} {start} to {end}')
        hanoi(n-1, by, start, end)
