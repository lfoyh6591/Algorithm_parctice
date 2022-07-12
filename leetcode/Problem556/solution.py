class Solution:
    def nextGreaterElement(self, n: int) -> int:
        max_int = 2**31-1
        n = str(n)
        n_list = list(n)
        n_list.reverse()
        length = len(n_list)
        st = []
        for i in range(length):
            if st and n_list[st[-1]] > n_list[i]:
                while st and n_list[st[-1]] > n_list[i]:
                    min_index = st.pop()
                n_list[min_index], n_list[i] = n_list[i], n_list[min_index]
                l = n_list[0:i]
                l.reverse()
                n_list[0:i] = l
                n_list.reverse()
                n = int(''.join(n_list))
                if n > max_int:
                    return -1
                else:
                    return int(''.join(n_list))

            st.append(i)

        return -1