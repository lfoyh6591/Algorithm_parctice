class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            minstr = s
            for i in range(len(s)):
                newstr = s[i+1:] + s[:i+1]
                if minstr > newstr:
                    minstr = newstr

            return minstr
        else:
            return "".join(sorted(s))