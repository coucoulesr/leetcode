# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix):
        height, width = binaryMatrix.dimensions()
        if height == 0 or width == 0:
            return -1
        x, y = width - 1, 0
        while y < height:
            if x < 0:
                return 0
            value = binaryMatrix.get(y,x)
            if value == 1:
                x -= 1
            else:
                y += 1
        return x + 1 if x + 1 < width else -1