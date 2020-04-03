class Solution:
    def isHappy(self, n):
        results = set()
        sum = 0
        while True:
            for i in str(n):
                sum += int(i) * int(i)
            if sum == 1:
                return True
            elif sum in results:
                return False
            elif sum not in results:
                results.add(sum)
                n = sum
                sum = 0

def main():
    sol = Solution()
    print(sol.isHappy(19))

if __name__ == "__main__":
    main()