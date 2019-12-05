"""
Leetcode Problem 014: Longest Common Prefix
Author: Richard Coucoules
Solved: 2019-12-04
"""


class Solution:
    def longestCommonPrefix(self, strs):
        output = ""
        if len(strs) == 0:
            return ""
        if len(strs[0]) == 0:
            return ""
        for i in range(2**32 - 1):
            try:
                letter = strs[0][i]
                for word in strs:
                    if word[i] != letter:
                        return output
                output += letter
            except IndexError:
                return output

def main():
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))    # Expect 'fl'
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))       # Expect ''
    print(sol.longestCommonPrefix([]))                              # Expect ''
    print(sol.longestCommonPrefix(["", "cat", "car"]))              # Expect ''
    print(sol.longestCommonPrefix(["hat", "hate", "hath"]))         # Expect 'hat'

if __name__ == "__main__":
    main()
