class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i, n in enumerate(nums):
            dic[target-n] = i

        for i, n in enumerate(nums):
            j = dic.get(n, -1)
            if (j >= 0) and (i != j):
                return [i, j]