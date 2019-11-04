"""
Leetcode Problem 002: Add Two Numbers
Author: Richard Coucoules
Solved: 2019-11-04
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None+

class Solution:
	def addTwoNumbers(self, l1, l2):
		listSum = self.linkedListToNum(l1) + self.linkedListToNum(l2)
		sumStr = str(listSum)
		liNode = ListNode(sumStr[0])
		for i in range(1, len(sumStr)):
			newNode = ListNode(sumStr[i])
			newNode.next = liNode
			liNode = newNode
		return liNode
		
	def linkedListToNum(self, ls):
		node = ls
		lsArray = [node.val]
		while node.next:
			node = node.next
			lsArray.append(node.val)
		lsArray.reverse()
		return int("".join([str(x) for x in lsArray]))
	