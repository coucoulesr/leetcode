"""
Leetcode Problem 283: Move Zeroes
Author: Richard Coucoules
"""  

class Solution:
    def moveZeroes(self, nums):
        idx = 0
        for _ in range(len(nums)):
            if nums[idx] == 0:
                nums.append(nums.pop(idx))
                continue
            idx += 1

def main():
    sol = Solution()
    nums = [0,1,0,3,12]
    print(nums)
    sol.moveZeroes(nums)
    print(nums)

if __name__ == "__main__":
    main()
