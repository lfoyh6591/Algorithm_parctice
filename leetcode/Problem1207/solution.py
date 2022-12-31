class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = {}
        for num in set(arr):
            if dic.get(arr.count(num), 0) != 0:
                return False
            else:
                dic[arr.count(num)] = 1

        return True