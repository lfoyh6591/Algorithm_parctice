class Solution:
    def binarysearch(self, start, end, nums, target):
        if start > end:
            return
        print(start, end)
        if (start >= len(nums)) or (end >= len(nums)):
            return
        if (nums[start] == target):
            if self.first!=-1:
                self.first = min(self.first, start)
            else:
                self.first = start
            if self.second == -1:
                self.second = start
        if (nums[end] == target):
            if self.first==-1:
                self.first = end
            if self.second != -1:
                self.second = max(self.second, end)
            else:
                self.second = end
        if start == end:
            return

        if (target >= nums[start]) and (target <= nums[end]):
            mid = (start + end) // 2
            self.binarysearch(start, mid, nums, target)
            self.binarysearch(mid+1, end, nums, target)
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        self.first = -1
        self.second = -1
        self.binarysearch(0, len(nums)-1, nums, target)
        return [self.first, self.second]