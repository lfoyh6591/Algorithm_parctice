class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zeros = nums.count(0)
        if zeros == 0:
            ret = [1]*len(nums)
            for i in range(1, len(nums)):
                ret[i] = ret[i-1]*nums[i-1]

            new_ret = [1]*len(nums)
            for i in range(len(nums)-2, -1, -1):
                new_ret[i] = new_ret[i+1]*nums[i+1]

            for i in range(len(nums)):
                ret[i] *= new_ret[i]
                
            return ret

        elif zeros == 1:
            cal = 1
            idx = -1
            for i in range(len(nums)):
                if nums[i] != 0:
                    cal *= nums[i]
                else:
                    idx = i
            ret = [0]*len(nums)
            ret[idx] = cal
            return ret
        
        else:
            return [0]*len(nums)