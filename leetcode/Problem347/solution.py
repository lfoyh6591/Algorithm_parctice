class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        dic = {}
        for i in range(len(nums)):
            if not dic.get(nums[i], 0):
                dic[nums[i]] = 1
                l = frequency.get(1, [])
                l.append(nums[i])
                frequency[1] = l
            else:
                dic[nums[i]] += 1
                l = frequency.get(dic[nums[i]], [])
                l.append(nums[i])
                frequency[dic[nums[i]]] = l
        
        frequencies = list(frequency.keys())
        frequencies.sort(reverse = True)

        for f in frequencies:
            if len(frequency[f]) < k:
                continue
            else:
                return frequency[f][:k+1]