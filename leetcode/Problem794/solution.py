class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix = [0]
        dic = {0 : 1}
        for i in range(len(nums)):
            prefix.append((prefix[i] + nums[i]) % k)
            dic[prefix[-1]] = dic.get(prefix[-1], 0) + 1
        
        ret = 0
        for v in dic.values():
            ret += (v*(v-1)//2)

        return ret