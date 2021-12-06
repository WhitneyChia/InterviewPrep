"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List


class Solution:
    """
    Not my solution, this is on leetcode
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    digits = "23"
    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert solution.letterCombinations(digits) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    # Example 2:
    digits = ""
    # Output: []
    assert solution.letterCombinations(digits) == []

    # Example 3:
    digits = "2"
    # Output: ["a", "b", "c"]
    assert solution.letterCombinations(digits) == ["a", "b", "c"]
