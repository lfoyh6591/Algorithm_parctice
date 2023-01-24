class Solution:
    def reverse(self, nums, start, end):
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        
        nums.reverse()
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)