class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        operators = ["+", "-", "*", "/"]
        cur = ""
        st = []
        for i, c in enumerate(s):
            if (c in operators):
                if not st:
                    st.append(int(cur))
                elif (st[-1] == "*"):
                    st.pop()
                    n = st.pop()
                    st.append(n*int(cur))
                elif (st[-1] == "/"):
                    st.pop()
                    n = st.pop()
                    st.append(n//int(cur))
                else:
                    st.append(int(cur))
                st.append(c)
                cur = ""
            else:
                cur += c

        if (not st) or (st[-1] not in operators):
            return int(cur)

        if (st[-1] == "*"):
            st.pop()
            n = st.pop()
            st.append(n*int(cur))
        elif (st[-1] == "/"):
            st.pop()
            n = st.pop()
            st.append(n//int(cur))
        else:
            st.append(int(cur))

        cur = st[0]
        for i in range(1, len(st)):
            if st[i] == "+":
                cur += st[i+1]
            elif st[i] == "-":
                cur -= st[i+1]
        
        return cur