class Solution:
    def lemonadeChange(self, bills) -> bool:
        wallet = []
        
        for bill in bills:
            wallet.append(bill)
            if bill == 10:
                if 5 in wallet:
                    wallet.remove(5)
                else:
                    return False
                
            elif bill == 20:
                if 5 in wallet:
                    wallet.remove(5)
                    if 10 in wallet:
                        wallet.remove(10)
                    else:
                        if 5 in wallet:
                            wallet.remove(5)
                            if 5 in wallet:
                                wallet.remove(5)
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
                
        return True
            