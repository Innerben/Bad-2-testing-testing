from entity import GameEntity
from random import choice

class Location(GameEntity):

    def __init__(self, name):
        super(Location, self).__init__(name)
        self.allowedOccupants = set()
        self.rooms = {}

    def addRooms(self, *rooms):
        for room in rooms:
            room.parent = self
            for purpose in room.getPurposes():
                if not purpose in self.rooms:
                    self.rooms[purpose] = []
                self.rooms[purpose].append(room)
            if not room.getPurposes():
                if not self.rooms.get(None):
                    self.rooms[None] = []
                self.rooms[None].append(room)
        return self

    def getRoom(self, actor, purpose):
        rooms = self.rooms.get(purpose)
        if rooms:
            validRooms = [room for room in rooms if room.canEnter(actor, purpose)]
            if validRooms:
                return choice(validRooms)
        return None

    def getRooms(self, actor, purpose):
        rooms = self.rooms.get(purpose)
        if rooms:
            return [room for room in rooms if room.canEnter(actor, purpose)]
        return None

    def getRandomRoom(self):
        allRooms = []
        for rooms in self.rooms.itervalues():
            for room in rooms:
                if not room.isFull():
                    allRooms.append(room)
        return choice(allRooms)

    def findRoom(self, name):
        foundRoom = None
        for rooms in self.rooms.itervalues():
            for room in rooms:
                if room.name == name:
                    foundRoom = room
        if not foundRoom:
            print "'{}' not found in {} '{}'".format(name, self, self.name)
        return foundRoom

    def onEnter(self, actor):
        room = self.getRandomRoom()
        room.onEnter(actor)

    def update(self):
        for rooms in self.rooms.itervalues():
            for room in rooms:
                room.update()
