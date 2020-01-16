from entity import GameEntity
from state import IdleState, SleepState, EatState, BatheState, SocializeState
from need import Need, Needs
from desire import Desires
from statistic import Statistics
from schedule import Schedule
from clock import Time

class Actor(GameEntity):
    
    needStates = {
        Need.ENERGY:    SleepState(),
        Need.HUNGER:    EatState(),
        Need.HYGIENE:   BatheState(),
        Need.SOCIAL:    SocializeState(),
        None:           IdleState()
    }
    
    def __init__(self, name, locationName, roomName):
        super(Actor, self).__init__(name)
        location = self.findEntity(locationName)
        room = location.findRoom(roomName)
        location.allowedOccupants.add(self)
        self.location = room
        self.home = room
        self.needs = Needs()
        self.desires = Desires()
        self.statistics = Statistics()
        self.schedule = Schedule()
        self.career = None
        self.careerLevel = None
        self.state = self.needStates[None]

    @property
    def priorityNeed(self):
        return self.needs.getPriorityNeed(self)

    def setCareer(self, careerName, careerLevel):
        self.career = self.findEntity(careerName)
        self.careerLevel = careerLevel

    def hasWorkToday(self, dayOfWeek):
        if self.career:
            return self.career.isWorkDay(self, dayOfWeek)
        return False

    def enter(self, location):
        self.exit()
        location.onEnter(self)

    def exit(self):
        if self.location is not None:
            self.location.onExit(self)

    def handleInput(self):
        state = self.state.handleInput(self, self.priorityNeed)
        if state is not None:
            self.state = state
            state.onEnter(self)

    def update(self, clock):
        self.needs.update()
        self.state.update(self)
        self.statistics.update(self, self.state.description, 1)
        self.schedule.execute(self, clock)
        if clock[Time.HOUR] == 1:
            self.schedule.update(self, clock.dayOfWeek)

    def onClick(self):
        print "{} clicked".format(self.name)