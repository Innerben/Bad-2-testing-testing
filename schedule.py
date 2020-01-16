from clock import Time
import event

class Schedule(object):

    def __init__(self):
        self.events = dict()

    def add(self, hour, event):
        self.events[hour] = event

    def update(self, actor, dayOfWeek):
        workTimes = actor.hasWorkToday(dayOfWeek)

        if workTimes:
            startTime = workTimes[0]
            endTime = workTimes[1]
            self.add(startTime, event.GoToWork)
            self.add(endTime, event.LeaveWork)

    def execute(self, actor, clock):
        event = self.events.get(clock[Time.HOUR], None)
        if event is not None:
            event(actor)

    def __getitem__(self, hour):
        return self.events.get(hour, None)