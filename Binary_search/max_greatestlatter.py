
"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0]."""

letters = ["c","f","j"]
target = "a"


def max_greater(letters,target):
    letters = list(dict.fromkeys(letters))
    print(letters)
    l = 0
    n = len(letters)
    h = n-1

    while l<=h:
        mid = (l+h)//2
        if ord(letters[mid]) == ord(target) and mid < n-2:
            return (letters[mid+1]) 
        elif ord(letters[mid]) > ord(target):
            h = mid - 1
        else:
            l = mid+1

    if h < 0 or h == n or l < 0 or l == n:
        return letters[0]
    else:
        return letters[l]

print(max_greater(letters,target))