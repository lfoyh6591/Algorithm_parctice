class MyCalendar:

    def __init__(self):
        self.booking = [[0, 0]]

    def book(self, starttime: int, endtime: int) -> bool:
        if len(self.booking) == 1:
            self.booking.append([starttime, endtime])
            return True
                
        start = 0
        end = len(self.booking) - 1
        
        while (end - start) > 1:
            mid = (start+end) // 2
            if self.booking[mid][0] > starttime:
                end = mid
            elif self.booking[mid][0] < starttime:
                start = mid
            else:
                return False
            
        if self.booking[end][0] < starttime:
            if self.booking[end][1] <= starttime:
                self.booking.append([starttime, endtime])
                return True
        else:
            if self.booking[start][1] > starttime:
                return False
            if self.booking[end][0] < endtime:
                return False
            self.booking.insert(end, [starttime, endtime])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)