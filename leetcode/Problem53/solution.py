class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre = [0] * (len(nums)+1)
        for i, v in enumerate(nums):
            pre[i+1] = pre[i] + v
        
        cur_min = pre[1]
        ret = pre[1]
        for v in pre[2:]:
            if cur_min < 0:
                ret = max(v - cur_min, ret, v)
            else:
                ret = max(v, ret)
            cur_min = min(v, cur_min)
        
        return ret