class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1
        ret = 0
        while end > start:
            ret = max(ret, min(height[end], height[start])*(end-start))

            if height[end] > height[start]:
                start += 1
            else:
                end -= 1

        return ret