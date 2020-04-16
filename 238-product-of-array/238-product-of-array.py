class Solution:
    def productExceptSelf(self, nums):
        l = [1 for _ in nums]
        r = [1 for _ in nums]
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
            r[-1-i] = r[-i] * nums[-i]
        output = []
        for i in range(len(nums)):
            output.append(l[i] * r[i])
        return output