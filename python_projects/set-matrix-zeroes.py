"""
Problem =
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

def setZeroes(matrix):
    """
    Modifies a matrix in-place by setting rows and columns to zero where zero values are found.

    Args:
    matrix (List[List[int]]): The input 2D matrix.

    Returns:
    None: The matrix is modified in-place.
    """

    # Find the coordinates of all zero elements and store them in separate lists
    zero_row_coordinates = []
    zero_column_coordinates = []
    
    for y_coo in range(len(matrix)):
        for x_coo in range(len(matrix[0])):
            if matrix[y_coo][x_coo] == 0:
                zero_row_coordinates.append(y_coo)
                zero_column_coordinates.append(x_coo)
    
    # Iterate through the matrix and set rows and columns to zero where zero elements were found
    for y_coo in range(len(matrix)):
        for x_coo in range(len(matrix[0])):
            if y_coo in zero_row_coordinates or x_coo in zero_column_coordinates:
                matrix[y_coo][x_coo] = 0

    return matrix

    
#Test functionality
print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))