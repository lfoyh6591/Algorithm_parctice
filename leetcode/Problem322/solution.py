class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memos = [0]*(amount+1)
        q = [(amount, 0)]
        if amount == 0:
            return 0
        while q:
            n, cnt = q.pop(0)
            if n in coins:
                return cnt+1

            for coin in coins:
                if n-coin < 0:
                    continue
                if memos[n-coin] == 0:
                    q.append((n-coin, cnt+1))
                    memos[n-coin] = 1

        return -1