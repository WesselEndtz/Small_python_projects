"""
Problem =
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""

def maxSatisfaction(satisfaction):
    sort_sati = list(sorted(satisfaction))
    non_negative = []
    negative = []
    for num in sort_sati:
        if num >= 0:
            non_negative.append(num)
        else:
            negative.insert(0, num)
    #print(negative, non_negative)
    def calculate_final(list_):
        ret = 0
        for x in range(len(list_)):
            ret += list_[x]*(x+1)
        return ret
    final_list = non_negative
    max_res = calculate_final(final_list)
    for x in negative:
        final_list.insert(0, x)
        res = calculate_final(final_list)
        if res > max_res:
            max_res = res
        else:
            return max_res
    return max_res
    
#Test functionality

print(maxSatisfaction([-1,-8,0,5,-7]))
print(maxSatisfaction([4,3,2]))
print(maxSatisfaction([-1,-4,-5]))