class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        st = [prices[0]]
        cur = prices[0]
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] < cur:
                x = st.pop()
                st.append(prices[i])
                ret += cur - x
            cur = prices[i]
        
        if st:
            x = st.pop()
            ret += cur - x

        return ret