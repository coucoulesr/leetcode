"""
Leetcode Problem 011: Container With Most Water
Author: Richard Coucoules
Solved: 2019-12-04
"""

# Brute Force solution: exceeds time limit
# class Solution:
#     def maxArea(self, height):
#         maxArea = 0
#         for (leftBound, leftVal) in enumerate(height):
#             for (rightBound, rightVal) in enumerate(height[leftBound + 1:], leftBound + 1):
#                 area = min(leftVal, rightVal) * (rightBound - leftBound)
#                 if area > maxArea:
#                     maxArea = area
#         return maxArea

class Solution:
    def maxArea(self, height):
        lIndex, rIndex = (0, len(height) - 1)
        lHeight, rHeight = (height[lIndex], height[rIndex])
        maxArea = min(lHeight, rHeight) * (len(height) - 1)
        while lIndex != rIndex:
            # Move the index with the lower value towards the other until it points to a higher value than before
            # Then see if the resulting area is larger
            incrementLeft = True if lHeight < rHeight else False
            if incrementLeft:
                lIndex += 1
                if height[lIndex] < lHeight:
                    continue
                lHeight = height[lIndex]
            else:
                rIndex -= 1
                if height[rIndex] < rHeight:
                    continue
                rHeight = height[rIndex]
            area = min(lHeight, rHeight) * (rIndex - lIndex)
            if area > maxArea:
                maxArea = area
        return maxArea


def main():
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))     # Expect 49
    print(sol.maxArea([2, 3, 4, 5, 18, 17, 6]))         # Expect 17
    print(sol.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) # Expect 25
    print(sol.maxArea([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Expect 25
    print(sol.maxArea([6, 7, 8, 9, 10, 1, 2, 3, 4, 5])) # Expect 45

    with open('test') as file:
        for line in file:
            print(sol.maxArea(list(map(int, line.split(','))))) # Expect 4959066, 48431514


if __name__ == "__main__":
    main()
