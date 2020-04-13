class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse = True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                del stones[1]
                del stones[0]
            else:
                stone = max(stones[0], stones[1]) - min(stones[0], stones[1])
                del stones[1]
                del stones[0]
                for i in range(len(stones) - 1, -1, -1):
                    if stones[i] > stone:
                        stones.insert(i + 1, stone)
                        break
                else:
                    stones.insert(0, stone)
        if not stones:
            return 0
        else:
            return stones[0]