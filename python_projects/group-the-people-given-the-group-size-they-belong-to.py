"""
Problem =
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""

def groupThePeople(groupSizes: list[int]) -> list[list[int]]:
    """
    Groups people based on their group sizes.

    Args:
    groupSizes (list[int]): A list of group sizes for each person.

    Returns:
    list[list[int]]: A list of groups where each group contains people with the same group size.
    """

    unique_group_sizes = sorted(set(groupSizes))  # Get unique group sizes
    
    final_groups = []  # Stores the final list of groups
    
    for size in unique_group_sizes:
        exist = True
        group = []
        
        while exist:
            person_index = groupSizes.index(size)
            group.append(person_index)
            groupSizes[person_index] = 0
            
            if size not in groupSizes:
                exist = False
            
            if len(group) == size and size in groupSizes:
                unique_group_sizes.append(size)
                exist = False
        
        final_groups.append(group)
    
    return final_groups


    
#Test functionality
print(groupThePeople([3,3,3,3,3,1,3]))
print(groupThePeople([2,1,3,3,3,2]))