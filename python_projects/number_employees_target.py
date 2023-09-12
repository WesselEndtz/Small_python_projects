"""
Problem =
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.
"""

def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    hours = sorted(hours)[::-1]
    num = 0
    for hour in hours:
        if hour < target:
            return num
        num += 1
    return num
    
#Test functionality
print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))