class SoundVariables():
    def __init__(self):
        print "Created new soundVariables class"
        self.SAMPLE_WIDTH = 2
        self.SAMPLE_RATE = 44100
        self.BIT_DEPTH = 65535 / 2
        self.CHANNELS = 2
        self.DURATION = 1 # seconds
        self.VOLUME = 0.9
        self.FREQUENCY = 2000  # Hz
        self.sampleLength = self.SAMPLE_RATE * self.DURATION

    def setValues(self, values):
        self.SAMPLE_WIDTH = values.SAMPLE_WIDTH
        self.SAMPLE_RATE = values.SAMPLE_RATE
        self.BIT_DEPTH = values.BIT_DEPTH
        self.CHANNELS = values.CHANNELS
        self.DURATION = values.DURATION
        self.VOLUME = values.VOLUME
        self.FREQUENCY = values.FREQUENCY
        self.sampleLength = self.SAMPLE_RATE * self.DURATION