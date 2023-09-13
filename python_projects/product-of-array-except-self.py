"""
Problem =
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
    """
    Computes the product of all elements in a list except for the element at the current index.

    Args:
    nums (List[int]): The input list of integers.

    Returns:
    List[int]: A list of integers where each element is the product of all elements in 'nums' except the one at the same index.
    """

    repeat = len(nums)
    
    # Initialize 'leftlist' to store products of elements to the left of the current element
    leftlist = [1]
    cur = 1
    for x in range(0, repeat - 1):
        cur *= nums[x]
        leftlist.append(cur)
    
    # Initialize 'rightlist' to store products of elements to the right of the current element
    rightlist = [1]
    cur = 1
    for x in range(1, repeat):
        cur *= nums[-x]
        rightlist.append(cur)
    
    # Calculate the final product list by multiplying corresponding elements from 'leftlist' and 'rightlist'
    final_list = []
    for x in range(repeat):
        final_list.append(leftlist[x] * rightlist[-(x + 1)])
    
    return final_list

    
#Test functionality
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))