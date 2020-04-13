# O(n^2) Brute Force
# class Solution:
#     def findMaxLength(self, nums):
#         longest = 0
#         for i in range(len(nums)):
#             count = {0: 0, 1: 0}
#             for j in range(i, len(nums)):
#                 count[nums[j]] += 1
#                 if count[0] == count[1] and count[0] + count[1] > longest:
#                     longest = count[0] + count[1]
#         return longest

# O(n) running total of 0s and 1s. Map 0 to -1 and 1 to 1 and sum. If running 
# total at index j is equal to running total at some previous index i, the 
# subarray nums[i:j] (inclusive) has equal number of 1s and zeros. Find
# subarray with max (j-i).
class Solution:
    def findMaxLength(self, nums):
        longest = 0
        sum = 0
        sums_found = {0: -1} # need to offset 0-indexing in arithmetic for j-i when i = 0
        for i in range(len(nums)):
            sum += nums[i] if nums[i] == 1 else -1
            if sum not in sums_found:
                sums_found[sum] = i
            else:
                longest = max(longest, i - sums_found[sum])
        return longest

def main():
    sol = Solution()
    print(sol.findMaxLength([]))  # 0
    print(sol.findMaxLength([0, 1]))  # 2
    print(sol.findMaxLength([0, 1, 0]))  # 2
    print(sol.findMaxLength([0, 1, 0, 1, 0, 1]))  # 6
    print(sol.findMaxLength([1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]))  # 6
    print(sol.findMaxLength([1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0]))  # 12


if __name__ == "__main__":
    main()
