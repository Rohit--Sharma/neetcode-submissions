class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = self.minstack[-1] if len(self.minstack) > 0 else float('inf')
        self.minstack.append(min(curr_min, val))

        # print(self.stack)
        # print(self.minstack)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
