class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        start = 0
        end = len(nums) - 1

        while end > start:
            mid = (start + end) // 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid+1

        return end