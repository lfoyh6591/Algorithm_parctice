class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(1, int(n**(1/2))+1)]
        dic = {n:0}
        q = [n]
        while q:
            k = q.pop(0)
            cnt = dic[k]
            for square in squares:
                if k-square == 0:
                    return cnt + 1

                if dic.get(k-square, 0):
                    continue
                
                dic[k-square] = cnt + 1
                q.append(k-square)

        return 0