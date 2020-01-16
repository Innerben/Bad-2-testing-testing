from entity import GameEntity
from clock import Time, Day

class Career(GameEntity):

    def __init__(self, name, location):
        super(Career, self).__init__(name)
        self.location = self.findEntity(location)
        self.roles = None

    def addRoles(self, *roles):
        self.roles = list()
        level = 0
        for role in roles:
            role.level = level
            self.roles.append(role)
            level += 1
        return self

    def findRole(self, title):
        for role in self.roles:
            if role.name == title:
                return role

    def getActorWorkHours(self, actor, dayOfWeek):
        role = self.roles[actor.careerLevel]
        if dayOfWeek in role.weekends:
            return None
        return (role.startTime, role.endTime)

class Role(object):

    def __init__(self, title, startTime, endTime, weekends = None):
        self.level = None
        self.name = title
        self.startTime = startTime
        self.endTime = endTime
        if not weekends:
            weekends = (Day.SATURDAY, Day.SUNDAY)
        self.weekends = weekends