class Solution:
    def search(self, nums, target):
        def binarySearch(nums, target, left_bound = 0):
            if not nums or (len(nums) == 1 and nums[0] != target):
                return -1
            if len(nums) == 2:
                if nums[0] == target:
                    return left_bound
                elif nums[1] == target:
                    return left_bound + 1
                else:
                    return -1 
            halfway = len(nums) // 2
            halfway_val = nums[halfway]
            if halfway_val == target:
                return halfway + left_bound
            else:
                target_bigger = True if target > halfway_val else False
                right_bigger = True if nums[halfway + 1] > halfway_val else False
                if right_bigger:
                    if target_bigger:
                        return binarySearch(nums[halfway + 1:len(nums)], target, left_bound + halfway + 1)
                    else:
                        return binarySearch(nums[0:halfway], target, left_bound)
                else:
                    if target_bigger:
                        return binarySearch(nums[0:halfway], target, left_bound)
                    else:
                        return binarySearch(nums[halfway + 1:len(nums)], target, left_bound + halfway + 1)
        def rotatedSearch(nums, target, left_bound = 0):
            if not nums or (len(nums) == 1 and nums[0] != target):
                return -1
            left, right, middle = nums[0], nums[len(nums) - 1], nums[len(nums) // 2]
            if target == middle:
                return left_bound + len(nums) // 2
            if target == left:
                return left_bound
            if target == right:
                return left_bound + len(nums) - 1
            if middle > left:
                if target > left and target < middle:
                    return binarySearch(nums[0:len(nums) // 2], target, left_bound)
                else:
                    return rotatedSearch(nums[(len(nums) // 2) + 1:len(nums)], target, left_bound + (len(nums) // 2) + 1)
            else:
                if target > middle and target < right:
                    return binarySearch(nums[(len(nums) // 2) + 1:len(nums)], target, left_bound + (len(nums) // 2) + 1)
                else:
                    return rotatedSearch(nums[0:len(nums) // 2], target, left_bound)
        return rotatedSearch(nums, target)              