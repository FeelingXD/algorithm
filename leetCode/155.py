# Min Stack
class MinStack(object):

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.minstack:
            self.minstack.append(val)
            self.stack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))
            self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.minstack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
