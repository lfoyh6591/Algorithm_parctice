from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        deq = deque()
        ret = []
        for i in range(len(nums)):
            if deq and deq[0] <= i-k:
                deq.popleft()

            while deq and nums[deq[0]] < nums[i]:
                deq.popleft()
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)

            if i>=k-1:
                ret.append(nums[deq[0]])

        return ret