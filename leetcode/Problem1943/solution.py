class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        dic = {}
        for start, end, color in segments:
            dic[start] = dic.get(start, 0) + color
            dic[end] = dic.get(end, 0) - color

        sort_key = sorted(dic.keys())
        prev_val = dic[sort_key[0]]
        prev_idx = sort_key[0]
        ans = []
        for key in sort_key[1:]:
            if prev_val != 0:
                ans.append([prev_idx, key, prev_val])
            prev_val += dic[key]
            prev_idx = key

        return ans