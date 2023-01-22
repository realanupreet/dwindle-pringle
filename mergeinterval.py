intervals = [[1, 4], [5,6]]

intervals.sort()
res = []

print("my intervals are", intervals)

if len(intervals) < 2:
    print("not happening")

start = intervals[0][0] # 1
end = intervals[0][1] # 4

for interval in intervals[1:]:
    print("->",interval)
    if interval[0] <= end:
        print(interval[0], "less than", end)
        cstart = start
        print("cstart becomes", cstart)
        cend = max(end, interval[1])
        print("cend becomes", cend)
    else:
        # cstart = interval[0]
        # cend = interval[1]
        print("in the else case")
        cstart = start
        cend = end
        start = interval[0]
        end = interval[1]
    start = cstart
    end = cend
    res.append([cstart, cend])

print(res)
