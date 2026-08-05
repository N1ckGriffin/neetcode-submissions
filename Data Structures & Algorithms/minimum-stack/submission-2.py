class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minTracker:
            self.minTracker.append(min(val, self.minTracker[-1]))
        else:
            self.minTracker.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minTracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minTracker[-1]
