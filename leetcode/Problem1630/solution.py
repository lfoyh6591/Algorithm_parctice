class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            if abs(l[i] - r[i]) < 2:
                res.append(True)
            
            else:
                n = nums[l[i]:r[i]+1]
                max_n = max(n)
                min_n = min(n)
                p = (max_n - min_n) // (r[i]-l[i])
                if p == 0:
                    state = True
                    for num in n:
                        if num != max_n:
                            state = False
                            break
                    res.append(state)
                    
                else:        
                    n_l = [0]*(r[i]-l[i]+1)
                    state = True
                    for num in n:
                        if (num-min_n)%p != 0:
                            state = False
                            break
                        else:
                            index = (num - min_n)//p
                            if index <= (r[i]-l[i]) and index >= 0 and n_l[index] == 0:
                                n_l[index] = 1
                            else:
                                state = False
                                break

                    res.append(state)
        
        return res