class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return True
        else:
            return self.canGetTo(nums, len(nums) - 1)
        
    def canGetTo(self, nums, idx):
        if idx == 0 and nums[idx] != 0:
            return True
        else:
            for i in range(1, len(nums[0:idx]) + 1):
                if nums[idx - i] >= i:
                    return self.canGetTo(nums, idx-i)
            return False