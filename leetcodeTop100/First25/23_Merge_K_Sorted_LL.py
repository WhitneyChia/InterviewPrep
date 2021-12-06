"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""
from typing import List, Optional


class ListNode:
    """
    # Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Not my code, leetcode's
    1) Most intuitive way is the same as 21_Merge_Two_sorted_Lists
        Just do this N - 1 times
        This however will be O(Nk), where k is the number is lists, O(1) space if done in place
    2) An improvement on this is divide and conquer
        Essentially merge sort
        This will be O(Nlogk) and O(1) space
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


if __name__ == "__main__":

    solution = Solution()

    # Example 1:
    list_1_head = ListNode(1)
    list_1_head.next = ListNode(4)
    list_1_head.next.next = ListNode(5)

    list_2_head = ListNode(1)
    list_2_head.next = ListNode(3)
    list_2_head.next.next = ListNode(4)

    list_3_head = ListNode(2)
    list_3_head.next = ListNode(6)

    # Output: [1, 1, 2, 3, 4, 4, 5, 6]
    result = solution.mergeKLists([list_1_head, list_2_head, list_3_head])
    curr = result
    solution = []
    while curr:
        solution.append(curr.val)
        curr = curr.next
    assert solution == [1, 1, 2, 3, 4, 4, 5, 6]
