class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx1 = 0
        idx2 = 0
        while (idx1 < n+m) and (idx2 < n):
            if (idx1 == m+idx2):
                nums1[idx1] = nums2[idx2]
                idx2 += 1
                idx1 += 1
                continue

            if nums1[idx1] > nums2[idx2]:
                nums1.insert(idx1, nums2[idx2])
                nums1.pop()
                idx2 += 1
                idx1 -= 1
            
            idx1 += 1