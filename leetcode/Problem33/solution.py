class Solution:
    def binarysearch(self, start, end, nums, target):
        print(start, end)
        if (nums[end] == target) or (nums[start] == target):
            return end if (nums[end] == target) else start
        else:
            if end <= start:
                return -1
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        if nums[start] > nums[end]:
            return max(self.binarysearch(mid+1, end, nums, target), self.binarysearch(start, mid-1, nums, target))
        else:
            if nums[mid] < target:
                return self.binarysearch(mid+1, end, nums, target)
            else:
                return self.binarysearch(start, mid-1, nums, target)
        
        return -1


    def search(self, nums: list[int], target: int) -> int:
        return self.binarysearch(0, len(nums)-1, nums, target)