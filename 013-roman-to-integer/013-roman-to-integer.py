"""
Leetcode Problem 013: Roman to Integer
Author: Richard Coucoules
Solved: 2019-12-04
"""

class Solution:
    def romanToInt(self, s):
        romanDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        output = 0
        revStr = s[::-1].upper()
        for i in range(len(revStr)):
            if i == 0:
                output += romanDict[revStr[i]]
                continue
            if romanDict[revStr[i]] < romanDict[revStr[i-1]]:
                output -= romanDict[revStr[i]]
            else:
                output += romanDict[revStr[i]]
        return output

def main():
    sol = Solution()
    print(sol.romanToInt('III'))        # Expect 3
    print(sol.romanToInt('IV'))         # Expect 4
    print(sol.romanToInt('IX'))         # Expect 9
    print(sol.romanToInt('LVIII'))      # Expect 58
    print(sol.romanToInt('MCMXCIV'))    # Expect 1994

if __name__ == "__main__":
    main()
