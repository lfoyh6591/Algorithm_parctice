class Solution:
    def rec(self, nums, lists):
        if not nums:
            return lists

        ret = []
        
        idx = 0
        for i in range(len(nums)):
            temp = nums.pop(i)
            lists2 = []
            if lists:
                for j in range(len(lists)):
                    lists2.append(lists[j]+[temp])
            else:
                lists2 = [[temp]]
            if ret:
                ret += self.rec(nums, lists2)
            else:
                ret = self.rec(nums, lists2)
            nums.insert(i, temp)

        return ret
        
    def permute(self, nums: list[int]) -> list[list[int]]:
        return self.rec(nums, [])