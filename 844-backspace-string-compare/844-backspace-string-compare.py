"""
Leetcode Problem 844: Backspace String Compare
Author: Richard Coucoules
"""  

class Solution:
    def backspaceCompare(self, S, T):
        s_arr, t_arr = [], []
        for ch in S:
            if ch == '#':
                if s_arr:
                    s_arr.pop()
                else:
                    continue
            else:
                s_arr.append(ch)
        for ch in T:
            if ch == '#':
                if t_arr:
                    t_arr.pop()
                else:
                    continue
            else:
                t_arr.append(ch)
        return t_arr == s_arr