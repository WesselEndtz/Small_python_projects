"""
Problem =
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

def threeSumClosest(nums, target):
    nums.sort()
    res = 0
    Best_diff = 999999
    print(nums)
    for i in range(len(nums)):
        left, right = i+1, len(nums)-1
        while left < right:
            #print(i, left, right)
            #print(nums[i], nums[left], nums[right])
            total = nums[i] + nums[left] + nums[right]
            if total > target:
                right -= 1
                diff = abs(target - total)
                if diff < Best_diff:
                    res = total
                    Best_diff = diff
            elif total < target:
                left += 1
                diff = abs(target - total)
                if diff < Best_diff:
                    res = total
                    Best_diff = diff
            else:
                res = total
                break
            #print("difference between numbers : " + str(diff), "calculation : " + str(target) + " and " + str(total))
    return res
    
#Test functionality

print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))