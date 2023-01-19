class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        dic = {}
        ret = 1
        for num in nums:
            if dic.get(num, 0) != 0:
                continue
            cal = dic.get(num-1, 0) + dic.get(num+1, 0) + 1
            ret = max(ret, cal)
            dic[num] = ret
            dic[num - dic.get(num-1, 0)] = cal
            dic[num + dic.get(num+1, 0)] = cal

        return ret