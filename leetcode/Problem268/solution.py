class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = sum(nums)
        n = len(nums)
        return (n*(n+1)//2) - s