"""
Problem =
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""

def targetIndices(nums: list[int], target: int) -> list[int]:
    """
    Finds the indices of all occurrences of a target value in a list of numbers.

    Args:
    nums (list[int]): The input list of numbers.
    target (int): The target value to search for in the list.

    Returns:
    list[int]: A list of indices where the target value is found in the input list.
    """

    # Create a sorted copy of the input list
    sorted_nums = list(sorted(nums))
    
    # Initialize a list to store the locations where the target value is found
    locations = []

    # Continue searching for the target value in the sorted list
    while target in sorted_nums:
        # Find the index of the target value in the sorted list
        location = sorted_nums.index(target)
        
        # Append the index to the locations list
        locations.append(location)
        
        # Replace the found target value in the sorted list with an empty string to avoid duplicates
        sorted_nums[location] = ''

    return locations


#Test functionality

print(targetIndices([1,2,5,2,3], 2))
print(targetIndices([1,2,5,2,3], 3))
print(targetIndices([1,2,5,2,3], 5))