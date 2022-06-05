
matrix = [[2,3,5],[4,0,7],[6,7,3]]
row0 = []
col0 = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            row0.append(i)
            col0.append(j)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i in row0 or j in col0:
            matrix[i][j] = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print("")


# 2  -> no. of test cases
# 2 3 ->  n and m 
# 7 19 3  
# 4 21 0
# 3 3
# 1 2 3
# 4 0 6
# 7 8 9