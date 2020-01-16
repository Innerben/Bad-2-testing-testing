from math import floor
from enum import Enum

class Time(Enum):
    HOUR =  1
    DAY =   2

class Day(Enum):
    SUNDAY =    0
    MONDAY =    1
    TUESDAY =   2
    WEDNESDAY = 3
    THURSDAY =  4
    FRIDAY =    5
    SATURDAY =  6

class UnitOfTime(object):

    def __init__(self, value, max, inHours, rollover):
        self.value = value
        self.max = max
        self.inHours = inHours
        self.rollover = rollover

class Clock(object):

    def __init__(self):
        self.units = {
            Time.HOUR:  UnitOfTime(value=8, max=24, inHours=1, rollover=Time.DAY),
            Time.DAY:   UnitOfTime(value=1, max=30, inHours=24, rollover=None)
        }
        self.totalHoursElapsed = 0

    def __getitem__(self, unitEnum):
        return self.units[unitEnum].value

    @property
    def dayOfWeek(self):
        dayNum = self.units[Time.DAY].value % 7
        return Day(dayNum)

    def advance(self, unitEnum, value, rollover=False):
        unit = self.units[unitEnum]
        newValue = unit.value + value
        if newValue > unit.max:
            if unit.rollover is not None:
                rolloverValue = int(floor(newValue / unit.max))
                self.advance(unit.rollover, rolloverValue, rollover=True)
            newValue = newValue % unit.max
        unit.value = newValue
        if not rollover:
            hoursElapsed = value * unit.inHours
            self.totalHoursElapsed += hoursElapsed
            return hoursElapsed

    def printTime(self):
        print "\n--------------DAY: {} HOUR: {}--------------\n" \
            .format(self[Time.DAY], self[Time.HOUR])