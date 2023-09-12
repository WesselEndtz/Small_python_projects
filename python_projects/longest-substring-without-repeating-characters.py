"""
Problem =
Given a string s, find the length of the longest 
substring
 without repeating characters.
"""

def lengthOfLongestSubstring(s):
    string = ''
    x = 0
    longest = 0
    result = 0
    while x < len(s):
        let = s[x]
        #If the letter is non repeating
        if let not in string:
            #Add the letter to the string
            string = string+let
            #we need to save the string if it is the longest one
            if len(string) > longest:
                result = len(string)
                longest = result
        else:
            #if it's a repeating letter we reset + do we need to go back the len() of string - 1 to make sure we don't miss, maybe? I don't know if that is a requirement, it is
            #We can also 
            x = x-len(string)
            string = ''
        x += 1
    return result
    
#Test functionality

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring("pwwkew"))