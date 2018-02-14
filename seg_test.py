class Segment():
    segment = 0
    def __init__(self, segment):
        self.segment = segment

    def setLeds(self, proc):
        print(self.segment)
        print(proc)

seg1 = Segment(1)

seg1.setLeds(2)
