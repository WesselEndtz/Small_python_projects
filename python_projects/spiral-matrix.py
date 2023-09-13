"""
Problem =
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

def spiralOrder(matrix):
    """
    Returns a list of elements in spiral order from a 2D matrix.

    Args:
    matrix (List[List[int]]): The input 2D matrix.

    Returns:
    List[int]: A list of elements in spiral order.
    """

    result = []  # Stores the elements in spiral order
    
    # Initialize variables to keep track of the boundaries
    horizon = 0
    vertic = 0
    max_horizon = len(matrix[0])
    max_vertic = len(matrix)
    min_horizon = 0
    min_vertic = 0
    three_sides = max_horizon + max_vertic - 2 + max_horizon - 1
    
    for x in range(max_horizon * max_vertic):
        result.append(matrix[vertic][horizon])
        
        # Update the direction of movement based on boundaries
        if horizon < max_horizon - 1 and vertic == min_vertic:
            horizon += 1
            if horizon == max_horizon - 2 and x >= three_sides:
                max_horizon -= 1
        elif vertic < max_vertic - 1 and horizon == max_horizon - 1:
            vertic += 1
            if vertic == max_vertic - 2 and x >= three_sides:
                max_vertic -= 1
        elif horizon > min_horizon and vertic == max_vertic - 1:
            horizon -= 1
            if horizon == min_horizon + 1 and x >= three_sides:
                min_horizon += 1
        elif vertic > min_vertic and horizon == min_horizon:
            vertic -= 1
            if vertic == min_vertic + 1 and x >= three_sides:
                min_vertic += 1
    
    return result


    
#Test functionality
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))