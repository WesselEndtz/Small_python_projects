"""
Problem =
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.
"""

def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    """
    Calculates the number of employees who met or exceeded a target number of hours worked.

    Args:
    hours (list[int]): A list of hours worked by employees.
    target (int): The target number of hours to meet or exceed.

    Returns:
    int: The number of employees who met or exceeded the target hours.
    """

    # Sort the list of hours in descending order for efficient traversal
    hours = sorted(hours, reverse=True)
    
    num_employees_met_target = 0  # Stores the number of employees who met or exceeded the target
    
    for hour in hours:
        if hour < target:
            # If an employee's hours are less than the target, stop counting and return the result
            return num_employees_met_target
        num_employees_met_target += 1
    
    return num_employees_met_target

    
#Test functionality
print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))