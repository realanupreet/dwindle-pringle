heights = [5, 1, 2, 3, 4]
h = sorted(heights)
occ = 0
for i in range(len(heights)):
    if h[i] != heights[i]:
        occ += 1
