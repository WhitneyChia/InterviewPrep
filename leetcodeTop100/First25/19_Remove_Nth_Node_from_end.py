"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        total_length = 0
        curr = head

        while curr:
            total_length += 1
            curr = curr.next

        # cover first node removal
        dummy_node = ListNode(next=head)

        target_node = total_length - n

        curr = dummy_node

        for i in range(0, total_length + 1):
            if i == target_node:
                break
            else:
                curr = curr.next

        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None

        return dummy_node.next


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2
    # Output: [1, 2, 3, 5]
    new_head = solution.removeNthFromEnd(head, n)
    curr = new_head
    ans = []
    while curr:
        ans.append(curr.val)
        curr = curr.next
    print(ans)

    # Example 2:
    head = ListNode(1)
    n = 1
    # Output: []
    new_head = solution.removeNthFromEnd(head, n)
    curr = new_head
    ans = []
    while curr:
        ans.append(curr.val)
        curr = curr.next
    print(ans)

    # Example 3:
    head = ListNode(1)
    head.next = ListNode(2)
    n = 1
    # Output: [1]
    new_head = solution.removeNthFromEnd(head, n)
    curr = new_head
    ans = []
    while curr:
        ans.append(curr.val)
        curr = curr.next
    print(ans)
