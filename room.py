from entity import GameEntity
from button import ButtonSpotList

class Room(GameEntity):

    def __init__(self, name):
        super(Room, self).__init__(name)
        self.name = name
        self.parent = None
        self.locked = False
        self.occupants = []
        self.buttonSpots = ButtonSpotList()

    def addButtonSpots(self, *spots):
        for spot in spots:
            self.buttonSpots.append(spot)
        return self

    def getPurposes(self):
        purposes = set()
        for spot in self.buttonSpots:
            purposes.add(spot.requiredState)
        return purposes

    def occupantCount(self, purpose = None):
        if not purpose:
            return len(self.occupants)
        count = 0
        for occupant in self.occupants:
            if occupant.state.fulfill == purpose:
                count += 1
        return count

    def occupantMax(self, purpose = None):
        return self.buttonSpots.actorSlotCount(purpose)

    def canEnter(self, actor, purpose = None):
        allowed = self.isOccupantAllowed(actor)
        locked = self.locked
        full = self.isFull(purpose)

        if allowed and not locked and not full:
            return True
        return False

    def isOccupantAllowed(self, actor):
        public = not self.parent.allowedOccupants
        if actor in self.parent.allowedOccupants or public:
            return True
        return False

    def isFull(self, purpose = None):
        if not purpose:
            return not self.occupantCount() < self.occupantMax()
        else:
            return not self.occupantCount(purpose) < self.occupantMax(purpose)

    def onEnter(self, actor):
        actor.location = self
        self.occupants.append(actor)

    def onExit(self, actor):
        if actor in self.occupants:
            self.occupants.remove(actor)

    def update(self):
        self.buttonSpots.reset()
        for occupant in self.occupants:
            self.buttonSpots.update(occupant)

    def onClick(self):
        print "{} clicked".format(self.name)



