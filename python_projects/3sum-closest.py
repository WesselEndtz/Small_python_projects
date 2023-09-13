"""
Problem =
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

def threeSumClosest(nums, target):
    """
    Finds the closest possible sum of three numbers from a sorted list to a target value.

    Args:
    nums (list[int]): The sorted input list of numbers.
    target (int): The target value to get closest to using three numbers from the list.

    Returns:
    int: The closest possible sum of three numbers to the target value.
    """

    nums.sort()  # Sort the input list for efficient traversal
    closest_sum = 0  # Stores the closest sum found
    best_difference = float('inf')  # Stores the best difference between the target and the closest sum
    
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # Calculate the absolute difference between the target and the current sum
            difference = abs(target - current_sum)
            
            if current_sum > target:
                right -= 1
                if difference < best_difference:
                    closest_sum = current_sum
                    best_difference = difference
            elif current_sum < target:
                left += 1
                if difference < best_difference:
                    closest_sum = current_sum
                    best_difference = difference
            else:
                # If the current sum is equal to the target, return it as the closest sum
                return current_sum
    
    return closest_sum

    
#Test functionality

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))