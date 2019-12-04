"""
Leetcode Problem 007: Reverse Integer
Author: Richard Coucoules
Solved: 2019-12-04
"""

class Solution:
    def reverse(self, x):
        intStr = str(x)
        negative = True if intStr[0] == '-' else False
        if negative:
            memStr = intStr[1:]
        else:
            memStr = intStr
        revIntStr = memStr[::-1]
        if negative:
            revIntStr = '-' + revIntStr
        revInt = int(revIntStr)
        if (revInt > 2**31 - 1 or revInt < -(2**31)):
            return 0
        return revInt

def main():
    sol = Solution()
    print(sol.reverse(123))     # Expect 321
    print(sol.reverse(-123))    # Expect -321
    print(sol.reverse(120))     # Expect 21

if __name__ == "__main__":
    main()
