"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:

        running_stack = []

        parens = {"}": "{", "]": "[", ")": "("}

        for paren in s:
            if paren not in parens:
                running_stack.append(paren)
            else:
                try:
                    top_of_stack = running_stack[-1]
                    if top_of_stack != parens[paren]:
                        return False
                    running_stack.pop()
                except IndexError:
                    return False

        return len(running_stack) == 0
    

if __name__ == "__main__":
    
    solution = Solution()
    # Example 1:
    s = "()"
    # Output: true
    assert solution.isValid(s) is True
    
    # Example 2:
    s = "()[]{}"
    # Output: true
    assert solution.isValid(s) is True 

    # Example 3:
    s = "(]"
    # Output: false
    assert solution.isValid(s) is False

    # Example 4:
    s = "([)]"
    # Output: false
    assert solution.isValid(s) is False

    # Example 5:
    s = "{[]}"
    # Output: true
    assert solution.isValid(s) is True



