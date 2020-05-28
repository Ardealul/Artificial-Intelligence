# return the transposed of matrix x
def transposed(x):
    y = []
    noCols = len(x[0])
    noRows = len(x)
    for i in range(noCols):
        row = []
        for j in range(noRows):
            row.append(x[j][i])
        y.append(row)
    return y


# return the matrix obtain by multiplication between x and y
def multiply(x, y):
    z = []
    noColsX = len(x[0])
    noRowsX = len(x)
    noColsY = len(y[0])
    noRowsY = len(y)
    # if noCols of x is not equal to noRows of y, it cannot exist a multiplication between x and y
    if noColsX != noRowsY:
        print("Cannot multiply X with Y!")
        return

    for i in range(noRowsX):
        row = []
        for j in range(noColsY):
            a = 0.0
            for k in range(noColsX):
                a += x[i][k] * y[k][j]
            row.append(a)
        z.append(row)

    return z


# return the matrix x without line i and column j
def minor(x, i, j):
    y = []
    noCols = len(x[0])
    noRows = len(x)
    for m in range(noRows):
        if m != i:
            row = []
            for n in range(noCols):
                if n != j:
                    row.append(x[m][n])
            y.append(row)
    return y


# return the determinate of a matrix x
def determinant(x):
    noCols = len(x[0])
    noRows = len(x)
    if noCols != noRows:
        print("Cannot determinate delta! No square matrix!")
        return
    # order of matrix is 2
    if noRows == 2:
        result = x[0][0] * x[1][1] - x[0][1] * x[1][0]
        return result
    # order of matrix is 3
    elif noRows == 3:
        result = x[0][0] * determinant(minor(x, 0, 0))
        result -= x[0][1] * determinant(minor(x, 0, 1))
        result += x[0][2] * determinant(minor(x, 0, 2))
        return result
    # order of matrix is greater than 3
    else:
        print("Not implemented!")
        return


# return the inverse of matrix x
def inverse(x):
    noCols = len(x[0])
    noRows = len(x)
    if noCols != noRows:
        print("Cannot determinate the inverse! No square matrix!")
        return
    delta = determinant(x)
    # if delta is 0 we cannot find the inverse of the matrix
    if delta == 0:
        print("Matrix is not reversible!")
        return
    xt = transposed(x)
    y = []
    for i in range(noRows):
        row = []
        for j in range(noCols):
            a = ((-1) ** (i + j)) * determinant(minor(xt, i, j))
            row.append(a * (1 / delta))
        y.append(row)
    return y


# for transpose
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transposed(matrix))

# for multiply
# x = [[1, 2, 3], [1, 2, 1]]
# y = [[4], [5], [6], [7]]
# print("x = " + str(x))
# print("y = " + str(y))
# print("z = " + str(multiply(x, y)))

# for minor
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(minor(x, 1, 2))

# for determinant
# x = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
# print(determinant(x))

# for inverse
# x = [[1, -1, 1], [2, 0, 3], [1, 1, -2]]
# print(inverse(x))
