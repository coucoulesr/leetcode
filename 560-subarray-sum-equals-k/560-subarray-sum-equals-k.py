class Solution:
    def subarraySum(self, nums, k):
        if not nums:
            return 0
        sums = {}
        cum_sum = 0
        count = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum not in sums:
                sums[cum_sum] = [i]
            else:
                sums[cum_sum].append(i)
        print(sums)
        for s in sums.keys():
            if s == k:
                for _ in sums[s]:
                    count += 1
            if not s - k in sums:
                continue
            for idx in sums[s]:
                for i in sums[s - k]:
                    if i < idx:
                        count += 1
        return count