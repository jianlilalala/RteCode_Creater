class signal:
    def __init__(self,name,dlc,factor,offset,minValue,maxValue,unit = ''):
        self.name = name
        self.dlc = dlc
        self.factor = factor
        self.offset = offset
        self.minValue = minValue
        self.maxValue = maxValue
        self.unit = unit