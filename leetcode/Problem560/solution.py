class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0]*(n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]

        dic = {}
        ret = 0
        for i in range(n+1):
            if dic.get(pre_sum[i]-k, 0) > 0:
                ret+=dic[pre_sum[i]-k]
            
            dic[pre_sum[i]] = dic.get(pre_sum[i], 0) + 1
            
        return ret