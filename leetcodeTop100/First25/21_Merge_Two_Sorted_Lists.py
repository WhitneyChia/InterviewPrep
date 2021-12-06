"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Essentially the same as two pointers """

        # Establishing a sentinel helps for this problem, we will return sentinel.next
        prehead = ListNode(val=-51)
        prev = prehead
        l1_curr = l1
        l2_curr = l2

        while l1_curr and l2_curr:
            if l1_curr.val <= l2_curr.val:
                prev.next = l1_curr
                l1_curr = l1_curr.next
            else:
                prev.next = l2_curr
                l2_curr = l2_curr.next
            prev = prev.next

        # One ll is finished, just need to connect to the one that has nodes left
        # We can do this since both lls were sorted already
        prev.next = l1_curr if l1_curr is not None else l2_curr

        # return sentinel.next -> the head
        return prehead.next


if __name__ == "__main__":

    solution = Solution()
    # Example 1:
    list1_head = ListNode(1)
    list1_head.next = ListNode(2)
    list1_head.next.next = ListNode(4)
    list2_head = ListNode(1)
    list2_head.next = ListNode(3)
    list2_head.next.next = ListNode(4)
    # Output: [1, 1, 2, 3, 4, 4]
    new_head = solution.mergeTwoLists(list1_head, list2_head)
    curr = new_head
    solution = []
    while curr:
        solution.append(curr.val)
        curr = curr.next
    assert solution == [1, 1, 2, 3, 4, 4]
