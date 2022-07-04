class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        stack = []
        res = [-1]*length
        
        for i in list(range(length)) *2:
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            
            if res[i] == -1:
                stack.append(i)
                        
        return res