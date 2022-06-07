
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]


def maxmeet(start, end, n):
    nmap = {}
    for i in range(n):
        print(f"start {start[i]} end {end[i]}")
        if len(nmap) == 0:
            nmap[start[i]] = end[i]
        elif start[i] > nmap[sorted(nmap.keys())[-1]]:
            nmap[start[i]] = end[i]
    return len(nmap)
