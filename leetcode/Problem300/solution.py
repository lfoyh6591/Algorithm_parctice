class Solution:
    def binarysearch(self, l, start, end, n):
        if end < start:
            return end
        mid = (start+end)//2
        if (l[mid] < n) and (n <= l[mid+1]):
            return mid
        if (l[mid] >= n):
            return self.binarysearch(l, start, mid-1, n)
        else:
            return self.binarysearch(l, mid+1, end, n)

    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [nums[0]]
        for i in range(1, len(nums)):
            if lis[-1] < nums[i]:
                lis.append(nums[i])
            else:
                if len(lis) == 1:
                    lis[0] = nums[i]
                    continue
                idx = self.binarysearch(lis, 0, len(lis)-1, nums[i])
                lis[idx+1] = nums[i]
        return len(lis)