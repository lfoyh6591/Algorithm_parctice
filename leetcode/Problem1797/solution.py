class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.add = timeToLive
        self.d_key_id = {}
        self.d_key_time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d_key_id[tokenId] = currentTime
        self.d_key_time[currentTime] = self.d_key_time.get(currentTime, []) + [tokenId]
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.d_key_id.get(tokenId, (-1)*self.add)+self.add > currentTime:
            temp = self.d_key_id[tokenId]
            self.d_key_id[tokenId] = currentTime
            self.d_key_time[temp].remove(tokenId)
            if len(self.d_key_time[temp]) == 0:
                del self.d_key_time[temp]
            self.d_key_time[currentTime] =  self.d_key_time.get(currentTime, []) + [tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ret = 0
        for key in self.d_key_time.keys():
            if key >= currentTime:
                return ret
            
            if key+self.add > currentTime:
                ret += len(self.d_key_time[key])
            
        return ret


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)