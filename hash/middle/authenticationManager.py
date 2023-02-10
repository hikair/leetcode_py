# 1797
# 设计一个验证系统

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.map = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = currentTime + self.timeToLive


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map and self.map[tokenId] > currentTime:
            self.map[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        result = 0
        for time in self.map.values():
            if time > currentTime:
                result += 1
        return result

