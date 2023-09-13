"""
Problem =
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""

function
    
#Test functionality
print(minPartitions("82734"))
print(minPartitions("27346209830709182346"))
print(minPartitions("32"))