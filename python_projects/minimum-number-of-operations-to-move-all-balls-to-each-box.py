"""
Problem =
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
"""

def minOperations(boxes: str) -> list[int]:
    """
    Calculates the minimum number of operations required to move all the balls to a box with a ball.

    Args:
    boxes (str): A string containing '0's and '1's, where '1' represents a box with a ball.

    Returns:
    list[int]: A list where each element represents the minimum number of operations to move balls to that box.
    """

    n = len(boxes)
    list_answ = [0] * n
    add = 0
    addition = 0

    # Calculate operations moving balls to the right
    for x in range(n):
        num = boxes[x]
        addition = addition + add
        list_answ[x] = addition
        if num == '1':
            add += 1

    add = 0
    addition = 0

    # Calculate operations moving balls to the left
    for x in range(-n + 1, 1):
        num = boxes[-x]
        addition = addition + add
        list_answ[-x] = list_answ[-x] + addition
        if num == '1':
            add += 1

    return list_answ


#Test functionality
print(minOperations("001011"))
print(minOperations("110"))