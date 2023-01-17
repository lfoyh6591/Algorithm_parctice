class Solution:
    def canJump(self, nums: list[int]) -> bool:
        l = len(nums)
        last = l-1
        for i in range(1, l):
            if last <= nums[l-i-1] + l-i-1:
                last = l-i-1
        
        if last == 0:
            return True
        else:
            return False