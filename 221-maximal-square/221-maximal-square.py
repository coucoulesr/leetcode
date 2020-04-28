class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        if len(matrix) == 1:
            return 1 if '1' in matrix[0] else 0
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                if int(matrix[0][i]) == 1:
                    return 1
            return 0
        self.memo = [[-1 for _ in row] for row in matrix]
        self.max = 0
        for i in range(len(matrix)):
            self.memo[i][len(matrix[i]) - 1] = int(matrix[i][len(matrix[i]) - 1]  )
        for j in range(len(matrix[len(matrix) - 1])):
            self.memo[len(matrix) - 1][j] = int(matrix[len(matrix) - 1][j])
        self.biggestSquareTopLeft(0, 0, matrix)
        return self.max ** 2
        
    def biggestSquareTopLeft(self, y, x, matrix):
        if self.memo[y][x] >= 0:
            if self.memo[y][x] > self.max:
                self.max = self.memo[y][x]
            return self.memo[y][x]
        elif int(matrix[y][x]) == 0:
            self.memo[y][x] = 0
            self.biggestSquareTopLeft(y, x+1, matrix)
            self.biggestSquareTopLeft(y+1, x, matrix)
            self.biggestSquareTopLeft(y+1, x+1, matrix)
            return self.memo[y][x]
        else:
            self.memo[y][x] = 1 + min(
                self.biggestSquareTopLeft(y, x+1, matrix),
                self.biggestSquareTopLeft(y+1, x, matrix),
                self.biggestSquareTopLeft(y+1, x+1, matrix)
                                )
            if self.memo[y][x] > self.max:
                self.max = self.memo[y][x]
                self.idx = (y, x)
            return self.memo[y][x]