class UndergroundSystem:
    def __init__(self):
        self.active = {} # id > (start, start_time)
        self.routes = [] # (start, end, duration)
        pass
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active[id] = (stationName, t)
        pass
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.active.pop(id)
        self.routes.append((start, stationName, t - start_time))
        pass
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        durations = []

        for start, end, duration in self.routes:
            if start == startStation and end == endStation:
                durations.append(duration)

        return sum(durations) / len(durations)
        pass
