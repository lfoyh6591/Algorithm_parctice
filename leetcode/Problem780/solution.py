class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while True:
            print(tx, ty)
            if tx*ty == 0:
                return False

            if tx==ty:
                if tx != sx:
                    return False
                else:
                    return True

            if (tx==sx) and (ty == sy):
                return True
            
            if tx == sx:
                if (ty > sy) and (ty-sy)%tx == 0:
                    return True
                else:
                    return False

            if ty == sy:
                if (tx > sx) and (tx-sx)%ty == 0:
                    return True
                else:
                    return False
            
            if tx > ty:
                tx %= ty
            else:
                ty %= tx