class UndergroundSystem:

    def __init__(self):
        self.avgs = {} # (start, end) = [avg, number of places]
        self.people = {} # id -> [place, time] or []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.people[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.people[id][0]
        startTime = self.people[id][1]
        
        trip = (start, stationName)
        if trip in self.avgs:
            avg = self.avgs[trip][0]
            amt = self.avgs[trip][1]
            total = avg * amt + t - startTime
            self.avgs[trip] = [total / (amt+1), amt+1]
        else:
            self.avgs[trip] = [t - startTime, 1]
        self.people[id] = []
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avgs[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)