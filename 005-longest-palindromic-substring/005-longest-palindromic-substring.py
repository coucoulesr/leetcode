"""
Leetcode Problem 005: Longest Palindromic Substring
Author: Richard Coucoules
Solved: 2019-12-04
"""


class Solution:
    def longestPalindrome(self, s):
        """Returns the longest palindrome that is a substring of s.
        
        1. Populates a dictionary with characters in s as keys and array of indices where the character can be found in s as values.
            O(len(s)) iterations
            O(1) per dict insertion, O(1) per array append
            O(len(s))*O(1)*O(1) = O(len(s)) total

        2. Iterates through each character in s and finds proceeding duplicates of the character.
            O(len(s)) iterations
            O(1) per lookup
            O(len(s))*O(1) = O(len(s)) total

        2.1 Checks each of the proceeding duplicates to see if the substring from 
        the current character to the duplicate is a palindrome.
            Worst Case:
                Every character is a duplicate
                O(len(s) - idx) iterations
                O(1 + 2 + 3 + ... + len(s) - idx) total lookups

                O(len(s))*O(len(s)) total
        
        Result: O(len(s)) + O(len(s)) * O(len(s)^2) = O(len(s)^3 + len(s))
        """
        if len(s) == 0:
            return ''
        sCharDict = {}
        for (idx, char) in enumerate(s.lower()):
            if char in sCharDict:
                sCharDict[char].append(idx)
            else:
                sCharDict[char] = [idx]
        maxPalindromeLength = 0
        longestPalindrome = ''
        for (sIdx, char) in enumerate(s.lower()):
            if len(sCharDict[char]) == 1:
                continue
            else:
                for charIdx in sCharDict[char]:
                    if sIdx >= charIdx:
                        continue
                    memStr = s[sIdx: charIdx+1]
                    if (memStr == memStr[::-1] and len(memStr) > maxPalindromeLength):
                        longestPalindrome = memStr
                        maxPalindromeLength = len(memStr)
        return longestPalindrome if maxPalindromeLength > 0 else s[0]


def main():
    sol = Solution()
    print(sol.longestPalindrome(''))    # Expect ''
    print(sol.longestPalindrome('babad'))  # Expect 'bab' or 'aba'
    print(sol.longestPalindrome('cbbd'))    # Expect 'bb'
    print(sol.longestPalindrome('abcde'))    # Expect 'a'
    print(sol.longestPalindrome('abcdedcba'))    # Expect 'abcdedcba'
    print(sol.longestPalindrome('abcdedcbz'))    # Expect 'bcdedcb'


if __name__ == "__main__":
    main()
