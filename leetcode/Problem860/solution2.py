class Solution:
    def lemonadeChange(self, bills) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            elif bill == 20:
                if five == 0 or (ten == 0 and five < 3):
                    return False
                else:
                    if ten == 0:
                        five -= 3
                    else:
                        ten -= 1
                        five -= 1
            
        return True
            