class Solution:
    def stringShift(self, s, shift):
        if not s or len(s) == 1:
            return s
        cum_sum = 0
        output = ''
        for sh in shift:
            cum_sum += sh[1] if sh[0] > 0 else -sh[1]
        if cum_sum and cum_sum % len(s):
            tot_shift = cum_sum % len(s)
            if tot_shift > 0:
                output = s[-tot_shift::] + s[0:len(s)-tot_shift]
            elif tot_shift < 0:
                output = s[tot_shift::] + s[0:tot_shift]
        else: 
            return s
        return output