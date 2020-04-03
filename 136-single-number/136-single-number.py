class Solution:
    def singleNumber(self, nums):
        appears_once, appears_twice = set(), set()
        for i in nums:
            if i not in appears_once and i not in appears_twice:
                appears_once.add(i)
            elif i in appears_once:
                appears_once.remove(i)
                appears_twice.add(i)
        return appears_once.pop()