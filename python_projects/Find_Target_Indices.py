"""
Problem =

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