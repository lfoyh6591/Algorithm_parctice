class Solution:
    def binarysearch(self, nums, k):
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == k:
                return mid
            if nums[mid] < k:
                start = mid+1
            else:
                end = mid-1
        
        return start

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = sorted(nums[:k])
        start = 0
        end = len(l)
        ret = [l[-1]]

        while end < len(nums):
            idx = self.binarysearch(l, nums[end])
            l.insert(idx, nums[end])
            idx = self.binarysearch(l, nums[start])
            l.pop(idx)
            ret.append(l[-1])
            end+=1
            start+=1
        
        return ret