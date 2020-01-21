class Attribute(object):
    
    def __init__(self, value, maxValue=100, decayRate=0, threshold=1):
        self._value = value
        self.maxValue = maxValue
        self.threshold = threshold
        self.decayRate = decayRate

    def __add__(self, value):
        newValue = self.value + value
        return Attribute(newValue, self.maxValue, self.decayRate)

    def __sub__(self, value):
        newValue = self.value - value
        return Attribute(newValue, self.maxValue, self.decayRate)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, newValue):
        if newValue < 0:
            self._value = 0
        elif newValue > self.maxValue:
            self._value = self.maxValue
        else:
            self._value = newValue

    def decay(self):
        self.value -= self.decayRate

    def replenish(self, value):
        if self.value > 0:
            self.value += self.decayRate + value
        else:
            self.value += value

class AttributeGroup(object):

    def __getitem__(self, key):
        return self.attributes[key]

    def __setitem__(self, key, value):
        self.attributes[key].value = value

    def __str__(self):
        stringArray = []
        for key, attribute in self.attributes.items():
            stringArray.append(key.name)
            stringArray.append(': ')
            stringArray.append(str(attribute.value))
            stringArray.append('|')
        return "".join(stringArray)

class Modifier(object):

    def __init__(attributeName, multiplier):
        self.multiply
