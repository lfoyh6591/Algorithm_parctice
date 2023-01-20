class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return []
        
        dic = {}
        for i in range(len(nums)-2, -1, -1):
            j = 1
            l = []
            q = []
            while i + j < len(nums):
                if nums[i+j] >= nums[i]:
                    if nums[i+j] in q:
                        j += 1
                        continue
                    q.append(nums[i+j])
                    cur = dic.get(nums[i+j],  [])
                    l.append([nums[i], nums[i+j]])
                    if cur:
                        l += [[nums[i]] + c for c in cur]
                j += 1

            dic[nums[i]] = l

        ret = []
        for v in dic.values():
            ret.extend(v)        
        
        return ret