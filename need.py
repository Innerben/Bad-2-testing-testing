from enum import Enum
from attribute import Attribute, AttributeGroup

class Need(Enum):
    SOCIAL = 2
    HYGIENE = 4
    HUNGER = 8
    ENERGY = 16

class Needs(AttributeGroup):
    def __init__(self):
        self.attributes = {
            Need.ENERGY:    Attribute(value=100, decayRate=6.25),
            Need.HUNGER:    Attribute(value=0, decayRate=25),
            Need.HYGIENE:   Attribute(value=50, decayRate=5),
            Need.SOCIAL:    Attribute(value=0, decayRate=5, threshold=50)
        }

    def getPriorityNeed(self, actor, filtered = None):
        if not filtered:
            filtered = []
        priorityNeed = None
        priorityValue = 0
        for need, attribute in self.attributes.items():
            if need not in filtered and attribute.value < attribute.threshold and need.value > priorityValue:
                priorityNeed = need
                priorityValue = need.value
        if not priorityNeed:
            return None
        if not actor.location.parent.getRoom(actor, priorityNeed):
            filtered.append(priorityNeed)
            return self.getPriorityNeed(actor, filtered)
        return priorityNeed

    def decay(self):
        for need, attribute in self.attributes.items():
            attribute.decay()

    def update(self):
        self.decay()
