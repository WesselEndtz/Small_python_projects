"""
Problem =
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""

def targetIndices(nums: list[int], target: int) -> list[int]:
    sorted_nums = list(sorted(nums))
    locations = []
    while target in sorted_nums:
        location = sorted_nums.index(target)
        locations.append(location)
        sorted_nums[location] = ''
    return locations

#Test functionality

print(targetIndices([1,2,5,2,3], 2))
print(targetIndices([1,2,5,2,3], 3))
print(targetIndices([1,2,5,2,3], 5))