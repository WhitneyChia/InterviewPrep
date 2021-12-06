"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional


class ListNode:
    """
    # Definition for singly-linked list. We are given this by leetcode
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        We can apply elementary math here summing each respective node and tracking the carry.
        We can start at the head as the number is reversed and then move next
        """

        # Establish a dummy head node for the result, so we will return dummy.next
        sol_dummy_head = ListNode(0)
        sol_tail = sol_dummy_head

        # Initialize carry as 0
        carry = 0

        # While we still have numbers, we can do this with carry since it will only be 0 or 1
        while l1 or l2 or carry:

            # grab the values from the nodes of both, if either one of them is done, it is the same as 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # sum them up with the carry
            total = val1 + val2 + carry

            # if it is greater than 10, then we have a carry of 1 and the value is mod 10
            if total >= 10:
                carry = 1
                value = total % 10
            # if it is not greater than 10, we have a carry of 0 and the sum is our value
            else:
                carry = 0
                value = total

            # Create a node with that value and move forward on the result ll
            sol_tail.next = ListNode(value)
            sol_tail = sol_tail.next

            # Move forward on the two lls
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # we initialized an empty node as our dummy head for corner cases, our answer actually starts at the next node
        return sol_dummy_head.next


if __name__ == "__main__":

    solution = Solution()

    # Example 1
    l1_head = ListNode(2)
    l1_head.next = ListNode(4)
    l1_head.next.next = ListNode(3)
    l2_head = ListNode(5)
    l2_head.next = ListNode(6)
    l2_head.next.next = ListNode(4)

    # Explanation: 342 + 465 = 807, we return 7, 0, 8
    # Output: [7,0,8]

    solution_head = solution.addTwoNumbers(l1_head, l2_head)
    solution_as_array = []
    while solution_head:
        solution_as_array.append(solution_head.val)
        solution_head = solution_head.next
    print(solution_as_array)

    # Example 2
    l1_head = ListNode(0)
    l2_head = ListNode(0)

    # Output: [0]

    solution_head = solution.addTwoNumbers(l1_head, l2_head)
    solution_as_array = []
    while solution_head:
        solution_as_array.append(solution_head.val)
        solution_head = solution_head.next
    print(solution_as_array)

    # Example 3
    l1_head = ListNode(9)
    l1_head.next = ListNode(9)
    l1_head.next.next = ListNode(9)
    l1_head.next.next.next = ListNode(9)
    l1_head.next.next.next.next = ListNode(9)
    l1_head.next.next.next.next.next = ListNode(9)
    l1_head.next.next.next.next.next.next = ListNode(9)
    l2_head = ListNode(9)
    l2_head.next = ListNode(9)
    l2_head.next.next = ListNode(9)
    l2_head.next.next.next = ListNode(9)

    # Output: [8, 9, 9, 9, 0, 0, 0, 1]

    solution_head = solution.addTwoNumbers(l1_head, l2_head)
    solution_as_array = []
    while solution_head:
        solution_as_array.append(solution_head.val)
        solution_head = solution_head.next
    print(solution_as_array)
