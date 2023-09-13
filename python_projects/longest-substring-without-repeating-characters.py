"""
Problem =
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

def lengthOfLongestSubstring(s):
    """
    Returns the length of the longest substring without repeating characters in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repeating characters.
    """

    current_substring = ''  # Stores the current substring being processed
    start_index = 0  # Stores the starting index of the current substring
    max_length = 0  # Stores the length of the longest substring found so far
    result = 0  # Stores the final result

    while start_index < len(s):
        current_char = s[start_index]

        # If the current character is not in the current substring
        if current_char not in current_substring:
            # Add the character to the current substring
            current_substring += current_char

            # Update the maximum length if the current substring is longer
            if len(current_substring) > max_length:
                result = len(current_substring)
                max_length = result
        else:
            # If it's a repeating character, reset the current substring
            # and adjust the start_index to the position after the first occurrence
            first_occurrence_index = current_substring.index(current_char)
            start_index += (first_occurrence_index + 1)
            current_substring = ''

        start_index += 1

    return result

    
#Test functionality

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring("pwwkew"))