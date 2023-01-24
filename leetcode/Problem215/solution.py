class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if not nums:
            return -100001
        pivot = nums[0]
        small = []
        big = []
        for n in nums[1:]:
            if n <= pivot:
                small.append(n)
            else:
                big.append(n)
        if len(big) == k-1:
            return pivot
        elif len(big) > k-1:
            return self.findKthLargest(big, k)
        else:
            return self.findKthLargest(small, k-len(big)-1)