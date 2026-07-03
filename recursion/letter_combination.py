
from typing import List
def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: if the digits string is empty, return empty list
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result: List[str] = []
        
        # Backtracking function
        def backtrack(index: int, current: str) -> None:
            # Base case: if the combination is complete
            if index == len(digits):
                result.append(current)
                return
            
            possible_letters = digit_to_letters[digits[index]]
            for letter in possible_letters:
                # Append the current letter and move to next digit
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result