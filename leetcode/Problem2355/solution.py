class Solution:
    def cal_stack(self, stack):
        cur_i = stack[0][0]
        cur_v = stack[0][1]
        ret = 0
        if cur_i > cur_v:
            ret = (cur_v)*(cur_v+1)//2
        else:
            ret = (cur_v + cur_v - cur_i)*(cur_i+1)//2
        for i, v in stack[1:]:
            ret += (v + v - (i - cur_i) + 1)*(i-cur_i)//2
            cur_i = i

        return ret

    def maximumBooks(self, books: list[int]) -> int:
        max_book = 0
        cur_book = 0
        prev_book = 0
        stack = []
        for i, book in enumerate(books):
            while stack and (stack[-1][1] + (i - stack[-1][0]) >= book):
                stack.pop()
            stack.append((i, book))
            if prev_book < book:
                cur_book += book
            else:
                cur_book = self.cal_stack(stack)
            if max_book < cur_book:
                max_book = cur_book
            prev_book = book
        
        return max_book