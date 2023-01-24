class Solution:
    def rec(self, nums, idx):
        if idx >= len(nums):
            return 0

        if self.memos[idx] != -1:
            return self.memos[idx]
        
        if len(nums) - idx == 1:
            self.memos[idx] = nums[idx]
            return nums[idx]
        
        self.memos[idx] = max((nums[idx] + self.rec(nums, idx+2)), nums[idx+1] + self.rec(nums, idx+3))
        return self.memos[idx]

    def rob(self, nums: list[int]) -> int:
        self.memos = [-1] * len(nums)
        return self.rec(nums, 0)