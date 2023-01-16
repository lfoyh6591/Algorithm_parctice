class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        length = 0
        temp = x
        while temp != 0:
            length += 1
            temp //= 10

        start = length // 2
        while start != 0:
            n1 = x%(10**start)//(10**(start-1))
            n2 = x//(10**(length-start))%10
            print(n1, n2)
            if n1 != n2:
                return False
            start -= 1

        return True