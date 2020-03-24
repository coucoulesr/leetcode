"""
Leetcode Problem 015: 3Sum
Author: Richard Coucoules
"""  

# Exceeds Time Limit
# class Solution:
#     def threeSum(self, nums):
#         output = []
#         nums_dict = {}
#         for idx, val in enumerate(nums):
#             if val in nums_dict:
#                 nums_dict[val].append(idx)
#             else:
#                 nums_dict[val] = [idx]
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j == i:
#                     continue
#                 searching_for = -1 * (nums[i] + nums[j])
#                 if searching_for in nums_dict:
#                     already_considered = 0
#                     for idx in nums_dict[searching_for]:
#                         if idx == i:
#                             already_considered += 1
#                         if  idx == j:
#                             already_considered += 1
#                     if already_considered >= len(nums_dict[searching_for]):
#                         continue
#                     triplet = [nums[i], nums[j], searching_for]
#                     triplet.sort()
#                     if triplet not in output:
#                         output.append(triplet)
#         return output

def main():
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, 4]))

if __name__ == "__main__":
    main()
