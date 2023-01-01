class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers)-1
        while start < end:
            cal = numbers[start] + numbers[end]
            if cal == target:
                return [start+1, end+1]
            elif cal < target:
                start += 1
            elif cal > target:
                end -= 1

        return []