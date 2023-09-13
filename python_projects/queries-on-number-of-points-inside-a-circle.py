"""
Problem =
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""
from math import sqrt

def countPoints(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    ans_list = []
    for querie in queries:
        in_circle = 0
        for point in points:
            x_point, y_point = point[0], point[1]
            x_querie, y_querie, z_querie = querie[0], querie[1], querie[2]
            z_to_querie_from_point = sqrt((x_point-x_querie)**2 + (y_point-y_querie)**2)
            #print('distance', sqrt(z_to_querie_from_point))
            #print('point', x_point, y_point)
            #print('querie', x_querie, y_querie, z_querie)
            if z_to_querie_from_point <= z_querie:
                in_circle += 1
        ans_list.append(in_circle)
    return ans_list
        

#Test functionality
print(countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]))
print(countPoints([[1,1],[2,2],[3,3],[4,4],[5,5]], [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]))