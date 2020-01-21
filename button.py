from entity import Entity

class ButtonSpotList(object):
    
    def __init__(self):
        self.spots = []
        self.index = 0
        self.length = 0

    def __iter__(self):
        self.index = 0
        self.length = len(self.spots)
        return self

    def next(self):
        if self.index < self.length:
            result = self.spots[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.spots[index]

    def append(self, spot):
        self.spots.append(spot)

    def update(self, returnObject):
        for spot in self.spots:
            spotFound = spot.update(returnObject)
            if spotFound:
                return
        
    def reset(self):
        for spot in self.spots:
            spot.reset()

    def actorSlotCount(self, state = None):
        if state is None:
            return len(self.spots)
        count = 0
        for spot in self.spots:
            if spot.criteria == state:
                count += 1
        return count

class ButtonSpot(Entity):

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.returnObject = None
        self.criteria = None
        self.enabled = False

class LocationSpot(ButtonSpot):

    def __init__(self, xpos, ypos, destination):
        super(LocationSpot, self).__init__(xpos, ypos)
        self.destination = destination
        self.returnObject = None
        self.enabled = True

    def setDestination(self, locationName, roomName):
        self.destination = self.findEntity(locationName).findRoom(roomName)

    def update(self, location):
        pass

    def reset(self):
        pass

class ActorSpot(ButtonSpot):

    def __init__(self, xpos, ypos, actorState = None):
        super(ActorSpot, self).__init__(xpos, ypos)
        self.criteria = actorState
        
    def update(self, actorObject):
        spotFound = False
        if not self.enabled and actorObject.state.fulfill == self.criteria:
            spotFound = True
            self.enabled = True
            self.returnObject = actorObject
        return spotFound

    def reset(self):
        self.returnObject = None
        self.enabled = False

    #action [Return(button.returnObject), SensitiveIf(button.returnObject.unlocked)]