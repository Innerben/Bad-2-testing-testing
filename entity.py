class GameEntity(object):
    findEntityDelegate = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def setFindEntityDelegate(cls, delegate):
        cls.findEntityDelegate = delegate

    def findEntity(self, value, attr='name', type=None):
        return self.findEntityDelegate(value, attr, type)