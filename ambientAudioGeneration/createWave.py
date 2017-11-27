import wave
import math
import struct

from soundVariables import *

TAU = math.pi * 2

class CreateWave:

    def __init__(self):
        print "Loaded CreateWave"
        self.variables = SoundVariables()
        # Add numerical references for the different wave creation algorithms for easy referencing
        self.waveCreations = [
            self.sineWave,
            self.squareWave,
            self.sawToothWave
        ]

    def setValues(self, values):
        self.variables.setValues(values)

    def sineWave(self, frequency = None):
        frequency = frequency or self.variables.FREQUENCY
        values = []
        for i in range(0, self.variables.SAMPLE_RATE):
            value = math.sin(TAU * frequency * (float(i) / self.variables.SAMPLE_RATE)) *\
                    (self.variables.VOLUME * self.variables.BIT_DEPTH)
            # Clamp the value as it may go over/under
            value = min(value, self.variables.BIT_DEPTH)
            value = max(value, -self.variables.BIT_DEPTH)

            for j in xrange(0, self.variables.CHANNELS):
                values.append(value)

        return values

    def squareWave(self, frequency = None):
        frequency = frequency or self.variables.FREQUENCY
        values = []
        for i in range(0, self.variables.sampleLength):
            value = 4 * (math.sin(frequency * (float(i) / self.variables.SAMPLE_RATE)) *
                         (self.variables.VOLUME * self.variables.BIT_DEPTH)) / math.pi
            # Clamp the value as it was going over/under - but now clips
            value = min(value, self.variables.BIT_DEPTH)
            value = max(value, -self.variables.BIT_DEPTH)

            for j in xrange(0, self.variables.CHANNELS):
                values.append(value)

        return values

    def sawToothWave(self, frequency = None):
        frequency = frequency or self.variables.FREQUENCY
        values = []
        for i in range(0, self.variables.sampleLength):
            value = 2 * (math.sin(frequency * (float(i) / self.variables.SAMPLE_RATE)) *
                         (self.variables.VOLUME * self.variables.BIT_DEPTH)) / -math.pi
            # Clamp the value as it may go over/under
            value = min(value, self.variables.BIT_DEPTH)
            value = max(value, -self.variables.BIT_DEPTH)

            for j in xrange(0, self.variables.CHANNELS):
                values.append(value)

        return values

