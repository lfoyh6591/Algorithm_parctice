class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        
        state = 0
        
        for i in range(0, len(nums)-1):
            if state == 0:
                if nums[i+1] > nums[i]:
                    state = 1
                elif nums[i+1] < nums[i] :
                    state = -1
            
            elif state > 0:
                if nums[i+1] < nums[i]:
                    return False
                
            elif state < 0:
                if nums[i+1] > nums[i]:
                    return False
                
        return True    