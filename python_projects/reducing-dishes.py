"""
Problem =
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""

def maxSatisfaction(satisfaction):
    """
    Calculates the maximum total satisfaction that can be obtained by arranging tasks in a specific order.

    Args:
    satisfaction (list[int]): A list of satisfaction values for each task.

    Returns:
    int: The maximum total satisfaction.
    """

    # Sort the satisfaction values in ascending order
    sorted_satisfaction = sorted(satisfaction)
    
    # Separate non-negative and negative satisfaction values
    non_negative = []
    negative = []
    
    for num in sorted_satisfaction:
        if num >= 0:
            non_negative.append(num)
        else:
            negative.insert(0, num)
    
    def calculate_final(list_):
        # Calculates the total satisfaction for a given arrangement of tasks
        total_satisfaction = 0
        for x in range(len(list_)):
            total_satisfaction += list_[x] * (x + 1)
        return total_satisfaction
    
    final_list = non_negative
    max_total_satisfaction = calculate_final(final_list)
    
    # Try adding negative satisfaction values to the beginning of the list to maximize satisfaction
    for x in negative:
        final_list.insert(0, x)
        total_satisfaction = calculate_final(final_list)
        if total_satisfaction > max_total_satisfaction:
            max_total_satisfaction = total_satisfaction
        else:
            # If adding more negative values doesn't improve satisfaction, return the current maximum
            return max_total_satisfaction
    
    return max_total_satisfaction

    
#Test functionality

print(maxSatisfaction([-1,-8,0,5,-7]))
print(maxSatisfaction([4,3,2]))
print(maxSatisfaction([-1,-4,-5]))