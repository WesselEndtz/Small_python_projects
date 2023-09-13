"""
Problem =
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
"""


def increasingTriplet(nums):
    """
    Determines if there exists a subsequence of length 3 in the given list that is increasing.

    Args:
    nums (List[int]): The input list of integers.

    Returns:
    bool: True if there is a subsequence of length 3 that is increasing, otherwise False.
    """

    first = second = float('inf')  # Initialize 'first' and 'second' as positive infinity
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            # If we find a number greater than 'second', there's an increasing subsequence
            return True
    
    return False  # If no increasing subsequence is found

    
#Test functionality
print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([2,1,5,0,4,6]))
print(increasingTriplet([5,4,3,2,1]))
