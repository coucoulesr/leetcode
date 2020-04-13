"""
Leetcode Problem 273: Integer to English Words
Author: Richard Coucoules
"""  

class Solution:
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        output = ''
        groups_list = ['Thousand', 'Million', 'Billion']
        teens_list = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens_list = ['?Zeroty?', '?Tenty?', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        numbers_list = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        num_str = str(num)
        group = -1
        while True:
            if len(num_str) >= 3:
                mem_str = num_str[-3::]
                num_str = num_str[0: len(num_str) - 3]
            else:
                mem_str = ("000" + num_str)[-3::]
                num_str = ''
            mem_ints = [int(i) for i in mem_str]
            group_str = ''
            if mem_ints[0] != 0:
                group_str += numbers_list[mem_ints[0]] + ' Hundred'
                if mem_ints[1] or mem_ints[2]:
                    group_str += ' '
            if mem_ints[1] >= 2:
                group_str += tens_list[mem_ints[1]]
                if mem_ints[2]:
                    group_str += ' '
            elif mem_ints[1] == 1:
                group_str += teens_list[mem_ints[2]]
            if mem_ints[2] != 0 and mem_ints[1] != 1:
                group_str += numbers_list[mem_ints[2]]
            if group >= 0 and group_str:
                group_str += ' ' + groups_list[group] + ' '
            group += 1
            output = group_str + output
            if not num_str:
                break
        return output.strip()


def main():
    sol = Solution()
    int_0 = 10000000000
    int_1 = 1
    int_2 = 20
    int_3 = 50868
    int_4 = 12345
    int_5 = 1234567
    int_6 = 1234567891
    print("'" + sol.numberToWords(int_0) + "'")
    print("'" + sol.numberToWords(int_1) + "'")
    print("'" + sol.numberToWords(int_2) + "'")
    print("'" + sol.numberToWords(int_3) + "'")
    print("'" + sol.numberToWords(int_4) + "'")
    print("'" + sol.numberToWords(int_5) + "'")
    print("'" + sol.numberToWords(int_6) + "'")

if __name__ == "__main__":
    main()