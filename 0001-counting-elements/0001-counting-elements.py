"""
Leetcode Problem: Counting Elements
Author: Richard Coucoules
Solved: 2020-04-07
"""

class Solution:
    def countElements(self, arr):
        elements = set(arr)
        count = 0
        for i in arr:
            if i+1 in elements:
                count += 1
        return count

def main():
	sol = Solution()
	arr_1 = [1,2,3]
	arr_2 = [1,1,3,3,5,5,7,7]
	arr_3 = [1,3,2,3,5,0]
	arr_4 = [1,1,2,2]
	print(sol.countElements(arr_1))
	print(sol.countElements(arr_2))
	print(sol.countElements(arr_3))
	print(sol.countElements(arr_4))

if __name__ == '__main__':
	main()