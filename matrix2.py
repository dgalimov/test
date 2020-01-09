def matrix_spiral_print(M):
    lowerBound = 0
    upperBound = len(M) - 1
    totalCount = sum(len(element) for element in M)

    result = []

    while lowerBound <= upperBound:
        rightBound = len(M[lowerBound]) - lowerBound # maximum right index. Mimimum left index will be equal to lowerBound

        # going from left to right
        result += [M[lowerBound][element] for element in range(lowerBound, rightBound)]

        # going  from top to bottom (right side)
        if len(result) < totalCount:
            for i in range(lowerBound + 1, upperBound):
                result += [M[i][-1 - lowerBound]]

        # going from right to left
        if lowerBound != upperBound:
            result += [M[upperBound][element] for element in range(lowerBound, rightBound)][::-1]

        # going from bottom to top (left side)
        if len(result) < totalCount:
            for i in range(upperBound-1, lowerBound, -1):
                result += [M[i][lowerBound]]

        # updating our border counters
        lowerBound += 1
        upperBound -= 1

    print(*result)


grid = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
]

# testing
# Mlength = 1
# Msize = 10
# 
# grid = [[element for element in range(row * Mlength + 1, (row + 1) * Mlength + 1)] for row in range (Msize)]
# 
# for row in grid:
#     print(row)
# end testing

matrix_spiral_print(grid)
