class Statistics(object):

    def __init__(self):
        self.log = {}

    def update(self, entity, statName, value):
        if not self.log.get(statName):
            self.log[statName] = 0
        self.log[statName] += value