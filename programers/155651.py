def solution(book_time):
    schedule = [0]*1450
    time_table = [(int(i[0][0:2])*60+int(i[0][3:]), int(i[1][0:2])
                   * 60+int(i[1][3:])+10) for i in book_time]
    for i in time_table:
        for j in range(i[0], i[1]):
            schedule[j] += 1
    return max(schedule)
