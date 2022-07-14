class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        res = 0
        p = 1
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] < k:
                start = i
                end = i
                p = nums[i]
                for j in range(start+1, len(nums)):
                    if p * nums[j] < k:
                        p *= nums[j]
                        end = j
                    else:
                        break
                break
        
        if end != -1 and end >= start:
            res += (end - start + 1)
        
        for i in range(start, len(nums)):
            if end < i:
                end = i
                
            p = p//nums[i] if end!=i else 1
            
            for j in range(end+1, len(nums)):
                if p * nums[j] < k:
                    p *= nums[j]
                    end = j
                else:
                    break
            res += (end - i)
            
        return res