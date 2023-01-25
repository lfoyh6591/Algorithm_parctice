class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                return cur
            nums[cur] *= -1