from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum=0
        self.size=size
        self.queue = deque([])
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue)==self.size:
            self.sum-=self.queue.popleft()
        self.sum+=val
        self.queue.append(val)
        return 1.0*self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
