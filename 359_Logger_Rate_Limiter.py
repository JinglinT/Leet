class Logger:

    def __init__(self):
        self.map_m_t = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.map_m_t and timestamp - self.map_m_t[message] < 10:
            return False
        self.map_m_t[message] = timestamp
        return True
