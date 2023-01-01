class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        dic = {}
        for interval in intervals:
            dic[interval[0]] = dic.get(interval[0], 0) + 1
            dic[interval[1]] = dic.get(interval[1], 0) - 1
        
        keys = sorted(dic.keys())
        maximum = 0
        cur = 0
        for key in keys:
            cur += dic[key]
            if maximum < cur:
                maximum = cur

        return maximum