"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    row = ""
    n = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(n):
            row += str(matrix[i][j]) + "  "
        print(row)
        row = ""


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            #diagonal
            if (i == j):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #prevent shallow copies
    copy = [[m2[row][col] for col in range(len(m2[0]))] for row in range(len(m2))]

    for r in range(len(m1)):
        for c in range(len(m2[0])):
            m2[r][c] = 0
            for i in range(len(m2)):
                m2[r][c] += m1[r][i] * copy[i][c]



def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
