"""
Leetcode Problem 001: Two Sum
Author: Richard Coucoules
Solved: 2019-11-04
"""

class Solution:
	def twoSum(self, nums, target):
		numDict = {}
		for idx, num in enumerate(nums):
			numDict[num] = idx
		for idx, num in enumerate(nums):
			addend = target - num
			if addend in numDict and numDict[addend] != idx:
				return [idx, numDict[target - num]]
			

# Failure 2: Brute force solution fails run time limit
# class Solution:
# 	def twoSum(self, nums, target):
# 		numsMemory = [num for num in nums]
# 		for idx, val in enumerate(nums):
# 			if val > target:
# 				continue
# 			for i in range(len(nums)):
# 				if idx == i or nums[i] > target:
# 					continue
# 				if val + nums[i] == target:
# 					out = [idx, i]
# 					break
# 			else:
# 				continue
# 			break
# 		return out
				
			
# Failure 1: Assumed positive integers in array and positive target
# class Solution:
# 	def twoSum(self, nums, target):
# 		summands = []
# 		numsSorted = [num for num in nums]
# 		numsSorted.sort()
# 		numsSorted.reverse()
# 		varTarget = target
# 		for num in numsSorted:
# 			if num > varTarget:
# 				continue
# 			elif num <= varTarget:
# 				varTarget -= num
# 				summands.append(num)
# 		out = []
# 		numsMemory = [num for num in nums]
# 		for a in summands:
# 			out.append(numsMemory.index(a))
# 			numsMemory[numsMemory.index(a)] = None
# 		out.sort()
# 		return out
		
		
soln = Solution()
nums = [3, 2, 4]
target = 6

print(soln.twoSum(nums, target))