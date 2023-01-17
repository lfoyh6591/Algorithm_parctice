class Solution:
    def rec(self, nums, lists):
        if not nums:
            return lists
        
        lists2 = []
        for l in lists:
            lists2.append(l+[nums[0]])
        ret = self.rec(nums[1:], lists) + self.rec(nums[1:], lists2)
        
        return ret

    def subsets(self, nums: list[int]) -> list[list[int]]:
        return self.rec(nums, [[]])