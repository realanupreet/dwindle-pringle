def generate(self, numRows: int) -> List[List[int]]:
    # numRows = 5
    res = [[1]]

    for i in range(numRows-1):
        temp = [0] + res[-1] + [0]
        row = []
        for t in range(len(res[-1])+1):
            row.append(temp[t]+temp[t+1])
        res.append(row)
    return res
