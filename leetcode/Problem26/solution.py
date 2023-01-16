class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur = nums[0]
        k = 1
        idx = 1
        for i in range(len(nums)-1):
            if nums[idx] == cur:
                temp = nums.pop(idx)
                nums.append(temp)
            else:
                cur = nums[idx]
                k += 1
                idx += 1
            
        return k