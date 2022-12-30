class Solution:
    def cal_water(self, height):
        if not height:
            return 0

        water = 0
        wall = 0
        cur_max = 0
        cur_idx = 0
        for i, h in enumerate(height):
            if h >= cur_max:
                water += max(i - cur_idx - 1, 0) * cur_max
                water -= wall
                wall = 0
                cur_max = h
                cur_idx = i
            else:
                wall += h

        return water

    def trap(self, height: list[int]) -> int:
        max_height = max(height)
        max_idx = height.index(max_height)

        return (self.cal_water(height[:max_idx+1]) + self.cal_water(reversed(height[max_idx:])))
        