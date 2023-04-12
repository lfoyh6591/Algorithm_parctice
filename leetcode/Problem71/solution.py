class Solution:
    def simplifyPath(self, path: str) -> str:
        idx = 0
        s = ""
        l = []
        while idx < len(path):
            if path[idx] == "/":
                if s and (s != "."):
                    l.append(s)
                s = ""
                cnt = 1
                while (idx+cnt < len(path)) and path[idx+cnt] == '/':
                    cnt += 1
                
                idx += (cnt-1)
            else:
                s += path[idx]
            idx += 1

        if s and (s != "."):
            l.append(s)

        st = []
        for s in l:
            if s == "..":
                if st:
                    st.pop()
            else:
                st.append(s)

        return "/"+"/".join(st)