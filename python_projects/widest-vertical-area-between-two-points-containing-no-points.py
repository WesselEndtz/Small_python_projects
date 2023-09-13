"""
Problem =
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    """
    Calculates the maximum width of a vertical area formed by a set of points.

    Args:
    points (list[list[int]]): A list of points in the form [x, y].

    Returns:
    int: The maximum width of the vertical area.
    """

    # Extract the x-coordinates from the list of points
    x_coordinates = [point[0] for point in points]
    
    # Sort the x-coordinates in ascending order
    x_coordinates = sorted(x_coordinates)
    
    max_width = 0  # Stores the maximum width of the vertical area
    
    # Calculate the differences between consecutive x-coordinates
    for x in range(len(x_coordinates) - 1):
        diff = x_coordinates[x + 1] - x_coordinates[x]
        
        if diff > max_width:
            max_width = diff
    
    return max_width

    
#Test functionality

print(maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))