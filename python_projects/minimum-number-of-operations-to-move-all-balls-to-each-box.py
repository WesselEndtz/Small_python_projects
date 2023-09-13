"""
Problem =
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.
"""

def minOperations(boxes: str) -> list[int]:
    list_answ = [0]*len(boxes)
    add = 0
    addition = 0
    for x in range(len(boxes)):
        num = boxes[x]
        addition = addition+add
        list_answ[x] = addition
        if num == '1':
            add += 1
    #print(list_answ)
    add = 0
    addition = 0
    for x in range(-len(boxes)+1, 1):
        num = boxes[-x]
        addition = addition+add
        list_answ[-x] = list_answ[-x]+addition
        if num == '1':
            add += 1
        #print(num, addition, add)
    return list_answ

#Test functionality
print(minOperations("001011"))
print(minOperations("110"))