class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        memo = [[0]*(len(nums2)+1) for i in range(len(nums1)+1)]
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i][j+1], memo[i+1][j])

        return memo[0][0]