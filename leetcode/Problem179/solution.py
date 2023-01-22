class Solution:
    def quicksort(self, nums):
        if not nums:
            return ""

        if len(nums) == 1:
            return str(nums[0])

        pivot = str(nums[0])

        left = []
        right = []

        for num in nums[1:]:
            s_num = str(num)
            if pivot+s_num >= s_num+pivot:
                right.append(num)
            else:
                left.append(num)

        return self.quicksort(left) + str(pivot) + self.quicksort(right)

    def largestNumber(self, nums: list[int]) -> str:
        s = self.quicksort(nums)
        idx = -1
        for i, c in enumerate(s[:-1]):
            if c == "0":
                idx = i
            else:
                break
        return s[idx+1:]
