class Solution:
    def find_in_prefix(self, prefix):
        ret = max(prefix[1:])
        min_val = min(prefix[1:])
        
        p = 1
        cnt = 0
        if min_val < 0:
            for val in prefix:
                if val < 0:
                    cnt += 1
                    if p == 1:
                        p = val
                    else:
                        p = max(p, val)
        
        if cnt != 1:
            ret = max(ret, min_val // p)
        
        return ret

    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = []
        prefix = [1]
        state = 0
        for num in nums:
            if num == 0:
                state = 1
                if len(prefix) > 1:
                    l.append(prefix)
                    prefix = [1]
                continue
            prefix.append(prefix[-1]*num)
        if len(prefix) > 1:
            l.append(prefix)
        ret = self.find_in_prefix(l[0])
        for p in l:
            ret = max(self.find_in_prefix(p), ret)
        if state:
            ret = max(ret, 0)

        return ret