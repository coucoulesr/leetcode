"""
Leetcode Problem 876: Middle of the Linked List
Author: Richard Coucoules
"""  

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        fast = slow = head
        if not head.val:
            return None
        if not head.next:
            return head
        i = 1
        while fast.next:
            fast = fast.next
            if i % 2 == 0:
                slow = slow.next
            i += 1
        if i % 2 == 0:
            slow = slow.next
        return slow
