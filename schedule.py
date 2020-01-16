from clock import Time
import event

class Schedule(object):

    def __init__(self):
        self.events = dict()

    def isFree(self, startTime, endTime=None):
        if endTime:
            for hour in range(startTime, endTime+1):
                if self.events.get(hour) is not None:
                    return False
        else:
            return self.events.get(startTime) is None
    
    def add(self, hour, newEvent):
        if self.isFree(hour):
            self.events[hour] = newEvent

    def addBlock(self, startTime, endTime, startEvent, endEvent):
        self.add(startTime, startEvent)
        self.add(endTime, endEvent)
        for hour in range(startTime+1, endTime):
            self.add(hour, event.Busy)

    def update(self, actor, dayOfWeek):
        self.events.clear()
        workHours = actor.getWorkHours(dayOfWeek)
        if workHours:
            startTime = workHours[0]
            endTime = workHours[1]
            self.addBlock(startTime, endTime, event.GoToWork, event.LeaveWork)

    def handleInput(self, actor, clock):
        return self.events.get(clock[Time.HOUR], None)

    def __getitem__(self, hour):
        return self.events.get(hour, None)