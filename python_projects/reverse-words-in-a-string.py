"""
Problem =
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def reverseWords(s):
    """
    Reverses the words in a string while preserving spaces between words.

    Args:
    s (str): The input string.

    Returns:
    str: The string with reversed words.
    """

    # Split the input string into a list of words using space as a separator
    words = s.split(' ')
    
    # Remove any empty strings resulting from multiple spaces
    while "" in words:
        words.remove("")
    
    # Reverse the order of words in the list
    for x in range(int(len(words) / 2)):
        word1 = words[x]
        word2 = words[-(x + 1)]
        words[x] = word2
        words[-(x + 1)] = word1
    
    # Join the reversed words back into a single string with spaces between them
    return ' '.join(words)

    
#Test functionality
print(reverseWords("a good   example"))
print(reverseWords("  hello world  "))
print(reverseWords("the sky is blue"))