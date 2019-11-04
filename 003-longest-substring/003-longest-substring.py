"""
Leetcode Problem 003: Longest Substring Without Repeating Characters
Author: Richard Coucoules
Solved: 2019-11-04
"""



class Solution:
	def lengthOfLongestSubstring(self, s: str):
		if len(s) < 1:
			return 0
		
		maxLength = 0
		strBuffer = s[0]
		length = 1
		idx = 1
		beg = 0
		while idx < len(s):
			if s[idx] in strBuffer:
				# print("Match found at idx {}: {}".format(idx, s[idx]))
				maxLength = max(maxLength, length)
				beg = s.find(s[idx], beg)
				idx = beg + 2
				strBuffer = s[beg+1]
				beg += 1
				length = 1
				# print("Beginning: {}, index: {}".format(beg, idx))
				# print("strBuffer " +strBuffer +"\n")
			else:
				strBuffer += s[idx]
				# print("No match.\nstrBuffer {}, idx {} \n".format(strBuffer, idx))
				length += 1
				idx += 1 
		return max(maxLength, length)
	
# soln = Solution()
# print(soln.lengthOfLongestSubstring("solutione"))