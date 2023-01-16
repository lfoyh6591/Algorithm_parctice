class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            n1 = 2**i
            n2 = 2**(31-i)
            if ((n&n2)>>(31-2*i)) != (n&n1):
                if (n&n1):
                    n -= n1
                    n += n2
                else:
                    n -= n2
                    n += n1

        return n