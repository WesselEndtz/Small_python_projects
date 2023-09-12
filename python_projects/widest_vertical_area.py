"""
Problem =
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""

def maxWidthOfVerticalArea(points: list[list[int]]) -> int:
    x_list = []
    for point in points:
        x_list.append(point[0])
    x_list = list(sorted(x_list))
    max_diff = 0
    for x in range(len(x_list)-1):
        diff = x_list[x+1]-x_list[x]
        if diff > max_diff:
            max_diff = diff
    return max_diff
    
#Test functionality

print(maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))