"""
Leetcode Problem 008: String to Integer (atoi)
Author: Richard Coucoules
Solved: 2019-12-04
"""

class Solution:
    def myAtoi(self, s):
        """Returns integer representation of string.
        
        String may contain leading spaces and a leading sign (+/-).
        Any trailing non-integer characters are ignoreed.
        Returns 2^31 - 1 if resulting int is larger than 2^31 - 1.
        Returns -2^31 if resulting int is smaller than -2^31.
        
        Runs in O(n) time, where n is the length of the input string."""
        memStr = s.lstrip(" ")
        if memStr == '':
            return 0
        negative = True if memStr[0] == '-' else False
        if (memStr[0] == '-' or memStr[0] == '+'):
            memStr = memStr[1:]
        output = 0
        if len(memStr) > 0:
            nextCharIsInt = self.isInt(memStr[0])
            while nextCharIsInt:
                output = output * 10 + int(memStr[0])
                if len(memStr) == 1:
                    break
                memStr = memStr[1:]
                nextCharIsInt = self.isInt(memStr[0])
        output = -1 * output if negative else output
        if output > 2**31 - 1:
            return 2**31 - 1
        if output < -2**31:
            return -2**31
        return output

    def isInt(self, ch):
        try:
            int(ch)
            return True
        except ValueError:
            return False

def main():
    # for char in "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
    #     print(char + ": " + str(isInt(char)))
    sol = Solution()
    print(sol.myAtoi('42'))                 # Expect 42
    print(sol.myAtoi('   -42'))             # Expect -42
    print(sol.myAtoi('4193 with words'))    # Expect 4193
    print(sol.myAtoi('words and 987'))      # Expect 0
    print(sol.myAtoi('-91283472332'))       # Expect -2147483648
    print(sol.myAtoi('-'))                  # Expect 0
    print(sol.myAtoi(' '))                  # Expect 0

if __name__ == "__main__":
    main()
