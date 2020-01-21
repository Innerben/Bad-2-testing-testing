from abc import ABCMeta, abstractmethod
from need import Need
from random import choice

class ActorState(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def onEnter(self, actor):
        location = actor.location.parent.getRoom(actor, self.fulfill)
        if location:
            actor.enter(location)

    @abstractmethod
    def handleInput(self, actor, need):
        if not need:
            return actor.needStates[None]
            #add logic to handle desires
        if need.value > self.fulfill.value:
            return actor.needStates[need]
        if actor.needs[self.fulfill].value == 100:
            return actor.needStates[need]

    @abstractmethod
    def update(self, actor):
        if self.fulfill:
            actor.needs[self.fulfill].replenish(100)

class IdleState(ActorState):
    description = 'idle'
    fulfill = None

    def onEnter(self, actor):
        location = actor.location.parent.getRandomRoom()
        actor.enter(location)

    def handleInput(self, actor, need):
        if need:
            return actor.needStates[need]

    def update(self, actor):
        super(IdleState, self).update(actor)

class SleepState(ActorState):
    description = 'sleeping'
    fulfill = Need.ENERGY

    def onEnter(self, actor):
        super(SleepState, self).onEnter(actor)

    def handleInput(self, actor, need):
        return super(SleepState, self).handleInput(actor, need)

    def update(self, actor):
        actor.needs[self.fulfill].replenish(12.5)

class EatState(ActorState):
    description = 'eating'
    fulfill = Need.HUNGER

    def onEnter(self, actor):
        super(EatState, self).onEnter(actor)

    def handleInput(self, actor, need):
        return super(EatState, self).handleInput(actor, need)

    def update(self, actor):
        super(EatState, self).update(actor)

class BatheState(ActorState):
    description = 'bathing'
    fulfill = Need.HYGIENE

    def onEnter(self, actor):
        super(BatheState, self).onEnter(actor)

    def handleInput(self, actor, need):
        return super(BatheState, self).handleInput(actor, need)

    def update(self, actor):
        super(BatheState, self).update(actor)

class SocializeState(ActorState):
    description = 'socializing'
    fulfill = Need.SOCIAL

    def onEnter(self, actor):
        locations = actor.location.parent.getRooms(actor, self.fulfill)
        for location in locations:
            if location.occupantCount(self.fulfill) > 0:
                actor.enter(location)
                return
        if locations:
            actor.enter(choice(locations))

    def handleInput(self, actor, need):
        return super(SocializeState, self).handleInput(actor, need)

    def update(self, actor):
        for occupant in actor.location.occupants:
            if actor.id != occupant.id and occupant.state == self:
                actor.needs[self.fulfill].replenish(20)
                return

