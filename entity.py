class Entity(object):
    findEntityDelegate = None
    addEntitiesDelegate = None
    isPlayerDelegate = None

    def __init__(self, name):
        self.name = name

    def findEntity(self, value, parentValue=None, attr='name', type=None):
        return self.findEntityDelegate(value, parentValue, attr, type)

    def addEntities(self, *entities):
        self.addEntitiesDelegate(*entities)

    def isPlayer(self):
        return self.isPlayerDelegate(self)