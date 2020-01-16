from enum import Enum
from attribute import Attribute, AttributeGroup

class Desire(Enum):
    PHYSIQUE = 0
    SMARTS = 1
    FUN = 2

class Desires(AttributeGroup):
    def __init__(self):
        self.attributes = {
            Desire.PHYSIQUE:    Attribute(value=0),
            Desire.SMARTS:      Attribute(value=0),
            Desire.FUN:         Attribute(value=0),
        }