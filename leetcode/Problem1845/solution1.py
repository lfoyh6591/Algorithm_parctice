class SeatManager:

    def __init__(self, n: int):
        self.seat = [i+1 for i in range(n)]
            
    def reserve(self) -> int:
        ret = self.seat[0]
        self.seat.remove(ret)
        return ret
    
    def unreserve(self, seatNumber: int) -> None:
        low = 0
        high = len(self.seat) - 1
        
        while low <= high:
            mid = (low+high) // 2
            if self.seat[mid] > seatNumber:
                if mid == 0:
                    self.seat.insert(0, seatNumber)
                    return
                elif self.seat[mid-1] < seatNumber:
                    self.seat.insert(mid, seatNumber)
                    return
                else:
                    high = mid
                    
            else:
                if mid == len(self.seat)-1:
                    self.seat.insert(len(self.seat), seatNumber)
                    return
                elif self.seat[mid+1] > seatNumber:
                    self.seat.insert(mid+1, seatNumber)
                    return
                else:
                    low = mid
                    
        self.seat.insert(low, seatNumber)
                    
            
            
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)