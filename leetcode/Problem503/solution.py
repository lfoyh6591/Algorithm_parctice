class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        param =-1*((10**9)+1) 
        res = [param]*length
        
        for i in range(length):
            for j in range(i+1, length+1):
                if j == length:
                    for k in range(i):
                        if nums[k] > nums[i]:
                            res[i] = nums[k]
                            break
                        elif res[k] > nums[i]:
                            res[i] = res[k]
                            break
                    if res[i] == param:
                        res[i] = -1
                    
                elif nums[j] > nums[i]:
                    res[i:j] = [nums[j]]*(j-i)
                    i = j-1
                    break
                    
        return res