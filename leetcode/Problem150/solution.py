import math
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op = ["+", "-", "*", "/"]
        
        st = []
        for token in tokens:
            if token not in op:
                st.append(token)
            
            else:
                a = int(st.pop())
                b = int(st.pop())
                if token == "+":
                    st.append(a+b)
                elif token == "-":
                    st.append(b-a)
                elif token == "*":
                    st.append(a*b)
                elif token == "/":
                    st.append(math.trunc(b/a))
                    
        return st.pop()
                
        