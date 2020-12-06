'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
'''

'''
1 0 3 4
2 4 5 1
0 3 1 2
1 2 2 2
4 5 6 7

turns into

0 0 0 0
0 0 5 1
0 0 0 0
0 0 2 2
0 0 6 7


The main idea is to look at each value and place markers to determinate which row and columns
have a 0 so after we look at each value, we overwrite with 0's whereever the markers say so.
Now we could do this with O(M*N) space complexity by marking down each row,col in a seperate matrix.
Then at the end we use this 2nd matrix to zero out where needed in the original matrix.

We could reduce the space complexity to O(N) by eliminating this second matrix and use two arrays where one array
tracks the index of the row that needs to be zeroed and then another array that tracks the index of the columns that need to be zeroed.

Finally we can reduce the space complexity to O(1) by storing the markers in the original
matrix itself and skip creating two arrays by using the first row and first column in the matrix to store the markers.
What needs to happen first though is see if there are any zeroes in the first row and column and if so then
create a boolean that tracks if there's a zero in the first row and a boolean that tracks if there was a zero
in that first column. The first row will be the markers to zero out any columns and the first column will be the markers
that will zero out any of the rows. We scan the rest of the matrix as normal and overwrite the first row and column
with 0's anytime we come across a 0.
'''

def zero_matrix(matrix):
    '''
    - Check if there are any zeroes in the first row or column. Note that the first row actually tracks the columns to zero out
    and the first column tracks all of the rows to zero out
    - Scan the rest of the matrix (not the first row or column) and if we see a 0 at i,j
    then overwrite first_row[0][j] = 0 and overwrite first_column[i,0] = 0
    - Scan first_row and at every [0][j] then run zero_column(matrix, j)
    - Do the same but for first_column respectively
    - If there was a zero in either the first row or column back from step 1 then zero out the first column and/or
    row respectively
    '''
    row_marker_has_zero = False
    column_marker_has_zero = False
    for index,_ in enumerate(matrix[0]):
        if matrix[0][index] == 0:
            column_marker_has_zero = True
            break
    for index,_ in enumerate(matrix):
        if matrix[index][0] == 0:
            row_marker_has_zero = True
            break
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 0:
                # set column marker to 0 for corresponding column
                matrix[0][j] = 0
                # set row marker to 0 for corresponding row
                matrix[i][0] = 0
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            zero_column(matrix, j)
    import pdb; pdb.set_trace()
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            zero_row(matrix, i)
    if row_marker_has_zero:
        # remember that the row marker is a column
        zero_column(matrix, 0)
    if column_marker_has_zero:
        # remember that the column marker is a row
        zero_row(matrix, 0)
    return matrix


def zero_row(matrix, row):
    for index in range(len(matrix[row])):
        matrix[row][index] = 0

def zero_column(matrix, col):
    for index in range(len(matrix)):
        matrix[index][col] = 0


matrix = [[0,1,2],[1,4,5],[2,0,3],[1,2,2]]
print(zero_matrix(matrix))
assert zero_matrix(matrix) == [[0,0,0],[0,0,5],[0,0,0],[0,0,2]]
