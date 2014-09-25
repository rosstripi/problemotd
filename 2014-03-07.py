
def rotate_clockwise(matrix1):
    """Takes an NxN matrix and rotates it clockwise.
        Matrix must be 2D list."""

    matrix2 = [[None] * len(matrix1)] * len(matrix1[0])
    for r in range(len(matrix1)):
        for c in range(len(matrix1[r])):
            matrix2[c][(len(matrix1)-1)-r] = matrix1[r][c]
            print r,c,"\n",matrix2[r],matrix2[c]
        print "\n"
        for row in matrix2:
            print row
        print "\n"

    return matrix2


matrix = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

