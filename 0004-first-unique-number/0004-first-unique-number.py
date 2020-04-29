import collections
class FirstUnique:

    def __init__(self, nums):
        self.singles = collections.OrderedDict()
        self.duplicates = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        for val, count in self.singles.items():
            return val if count == 1 else -1
        return -1

    def add(self, value):
        if value in self.duplicates:
            return
        elif value in self.singles:
            del self.singles[value]
            self.duplicates.add(value)
        else:
            self.singles[value] = 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)