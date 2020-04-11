class MinStack:
    def __init__(self):
        self.min = float("inf")
        self.stack = []
        self.min_arr = []
        self.count = {}

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x in self.count:
            self.count[x] += 1
        else:
            self.count[x] = 1
        if x < self.min:
            self.min = x
            self.min_arr.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        if self.count[self.stack[-1]] == 1:
            if self.stack[-1] == self.min:
                del self.min_arr[-1]
                if self.min_arr:
                    self.min = self.min_arr[-1]
                else:
                    self.min = float("inf")
            del self.count[self.stack[-1]]
        else:
            self.count[self.stack[-1]] -= 1
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.min