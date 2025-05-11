'''
To check whether two strings are valid anagrams, we ensure both contain the same characters with the same frequency. For example:

"cat" and "tac" are anagrams.

"cat" and "dog" are not anagrams (letters differ).

✅ Approach 1: Brute Force (Sorting)
Step 1: Check if the lengths of the two strings are unequal. If yes, return False.
Step 2: Sort both strings.
Step 3: Compare the sorted strings and return the result.

Time Complexity:
O(n log n + m log m) due to sorting
Space Complexity:
O(n + m) for storing sorted strings (since strings are immutable in Python)

✅ Approach 2: Hash Map (Dictionary)
Step 1: Check if the lengths differ; return False if they do.
Step 2: Traverse both strings:
For the first string, count the frequency of each character using a dictionary.
For the second string, do the same.
Step 3: Compare both dictionaries.

Time Complexity: O(n)
Space Complexity: O(1)
Because we only store counts for up to 26 lowercase letters — constant space.

✅ Approach 3: Fixed-Size Array (Optimized Counting)
Use two arrays of size 26 (for lowercase letters a–z).
Step 1: If lengths differ, return False.
Step 2: Traverse both strings:
Increment the count for characters in the first string.
Decrement the count for characters in the second string.
Step 3: After traversal, if the array has all zeros, return True, else False.

Time Complexity: O(n)
Space Complexity: O(1)
Constant space because of the fixed-size array (26 letters).'''
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    '''
    if len(s)!=len(t):
        return False 
    
    return sorted(s)==sorted(t)'''

    '''

    if len(s)!=len(t):
        return False 
    
    hm_s, hm_t = {},{}
    for i in range(len(s)):
        hm_s[s[i]] = hm_s.get(s[i],0)+1
        hm_t[t[i]] = hm_t.get(t[i],0)+1
    return hm_s == hm_t'''

    if len(s)!=len(t):
        return False
    arr = [0]*26
    for i in range(len(s)):
        arr[ord(s[i])-ord('a')]+=1 
        arr[ord(t[i])-ord('a')]-=1
    
    for i in range(len(arr)):
        if arr[i]!=0:
            return False 
    return True
    
