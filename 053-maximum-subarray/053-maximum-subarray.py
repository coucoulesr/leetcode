"""
Leetcode Problem 053: Maximum Subarray
Author: Richard Coucoules
"""  


# O(n^3) solution: check every possible subarray and check the sum of each subarray
# 
# class Solution:
#     def maxSubArray(self, nums):
#         max_sum = float('-inf')
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 max_sum = sum(nums[i:j]) if sum(nums[i:j]) > max_sum else max_sum     # sum() is effectively another for loop through the subarray
#         return max_sum

# O(n^2) solution: use the fact that the sum of a array containing a subarray and its 
# neighbor is the sum of the subarray plus the neighbor, stop computing so many sums
# (i.e. sum(list[i:j]) = sum(list[i:j-1]) + list[j])
# that is, sum_total = sum_so_far + next_item
# 
# class Solution:
#     def maxSubArray(self, nums):
#         max_sum = float('-inf')
#         sum_so_far = 0
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 sum_so_far += nums[j]
#                 max_sum = sum_so_far if sum_so_far > max_sum else max_sum
#             sum_so_far = 0
#         return max_sum


# O(n) solution: dynamic programming - use the information about the best subarray that
# could be generated that ends at index i - 1 to see if the best subarray that could be
# generated at index i is an extension of the best subarray at i-1 or a new subarray
# containing only i.

class Solution:
    def maxSubArray(self, nums):
        max_subarray_at_idx = [0 for num in nums]
        max_subarray_at_idx[0] = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            max_subarray_at_idx[i] = max(nums[i], max_subarray_at_idx[i-1] + nums[i])
            max_sum = max_subarray_at_idx[i] if max_subarray_at_idx[i] > max_sum else max_sum
        return max_sum

def main():
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

if __name__ == "__main__":
    main()
