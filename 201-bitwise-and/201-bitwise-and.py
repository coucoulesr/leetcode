# Bitwise AND always returns number smaller than smaller operand
# If descending downwards, you will AND with the result anyways
# So you can skip to the result of the AND operation when descending
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n = n & n-1
        return m & n