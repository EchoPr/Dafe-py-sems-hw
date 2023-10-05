def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # Сканирующая прямая

    events = []
    for i in intervals:
        events.append([i[1], 1])
        events.append([i[0], -1])
    events.sort()

    res = []
    cnt = 0
    curl = -1

    for e in events:
        if e[1] == -1:
            cnt += 1
            if curl == -1: curl = e[0]
        else:
            cnt -= 1
            if cnt == 0:
                res.append([curl, e[0]])
                curl = -1

    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
assert merge_intervals(intervals) == [[1, 6],[8, 10],[15, 18]]

print(merge_intervals(intervals))


    
    


