class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        dic = {}
        
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1

        ret = []
        new_nums = sorted(list(set(nums)))
        
        for i in range(len(new_nums)):
            for j in range(len(new_nums)):
                cal = -new_nums[i]-new_nums[j]
                dic[new_nums[i]] -= 1
                dic[new_nums[j]] -= 1
                if dic.get(cal, 0) > 0:
                    if (cal >= new_nums[i]) and (cal <= new_nums[j]):
                        ret.append([new_nums[i], cal, new_nums[j]])        
                dic[new_nums[i]] += 1
                dic[new_nums[j]] += 1

        return ret