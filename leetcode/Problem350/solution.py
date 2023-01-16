class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic = {}
        for n in nums1:
            dic[n] = dic.get(n, 0)+1
        ret = []
        for n in nums2:
            if dic.get(n, 0) !=  0:
                ret.append(n)
                dic[n] -= 1

        return ret