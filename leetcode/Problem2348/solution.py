class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        idx = 0
        ans = 0
        zeros = 0
        while idx < len(nums):
            if zeros != 0:
                if nums[idx] == 0:
                    zeros += 1
                else:
                    ans += (zeros*(zeros+1)//2)
                    zeros = 0
            else:
                if nums[idx] == 0:
                    zeros += 1
            
            idx += 1
        
        ans += (zeros*(zeros+1)//2)
        
        return ans