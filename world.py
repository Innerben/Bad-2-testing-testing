from actor import Actor
from location import Location
from clock import Clock, Time
from random import shuffle, choice

class World(object):

    def __init__(self):
        self.entityId = 0   #last used entity id
        self.entities = dict()
        self.storedEntity = None
        self.clock = Clock()
        self.player = None

    def setPlayer(self, actor):
        self.player = actor

    def isPlayer(self, entity):
        return entity is self.player

    def addEntities(self, *entities):
        for entity in entities:
            if not type(entity) in self.entities:
                self.entities[type(entity)] = {}
            self.entities[type(entity)][self.entityId] = entity
            entity.id = self.entityId
            entity.world = self
            self.entityId += 1

    def findEntity(self, value, parentValue=None, attr='name', type=None, store=False):
        foundEntity = list()

        if type:
            for entity in self.entities[type].itervalues():
                if getattr(entity, attr, None) == value:
                    foundEntity.append(entity)
        else:
            for entityType in self.entities.itervalues():
                for entity in entityType.itervalues():
                    if getattr(entity, attr, None) == value:
                        foundEntity.append(entity)
        if not foundEntity:
            print "'{}' not found in {}".format(value, self)
            return
        if len(foundEntity) == 1:
            foundEntity = foundEntity[0]
        elif parentValue:
            for entity in foundEntity:
                if getattr(entity.parent, attr, None) == parentValue:
                    foundEntity = entity
        elif len(foundEntity) > 1:
            print "found multiple entities with '{}': '{}', returning list".format(attr, value)
        if store:
            self.storedEntity = foundEntity
        return foundEntity

    def update(self, hours=1):
        for hour in range(hours):
            self.advanceTime(Time.HOUR, 1)
            self.updateActors()
            self.updateLocations()

    def advanceTime(self, unitOfTime, units):
        self.clock.advance(unitOfTime, units)
        self.clock.printTime()

    def updateActors(self):
        actors = [actor for actor in self.entities[Actor].itervalues()]
        shuffle(actors)
        for actor in actors:
            actor.handleInput(self.clock)
            actor.update(self.clock)
        actors.sort(key=lambda actor: actor.id)
        for actor in actors:
            print "{}, {}, {}, {}".format(
                actor.name, 
                actor.location.name[0:3], 
                actor.state.description[0:3], 
                actor.needs
            )

    def updateLocations(self):
        for location in self.entities[Location].itervalues():
            location.update()