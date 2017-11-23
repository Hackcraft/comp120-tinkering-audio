import wave
import math
import struct
TAU = math.pi * 2

class CreateWave:

    def __init__(self):
        print "Loaded CreateWave"
        self.SAMPLE_WIDTH = 2
        self.SAMPLE_RATE = 44100
        self.BIT_DEPTH = 65535 / 2
        self.CHANNELS = 2
        self.DURATION = 5  # seconds
        self.VOLUME = 0.4
        self.FREQUENCY = 150  # Hz
        self.sampleLength = self.SAMPLE_RATE * self.DURATION

    def setValues(self, sampleWidth, sampleRate, bitDepth, channels, duration, volume, frequency):
        self.SAMPLE_WIDTH = sampleWidth
        self.SAMPLE_RATE = sampleRate
        self.BIT_DEPTH = bitDepth
        self.CHANNELS = channels
        self.DURATION = duration
        self.VOLUME = volume
        self.FREQUENCY = frequency
        self.sampleLength = self.SAMPLE_RATE * self.DURATION

    def sineWave(self, frequency = None):
        frequency = frequency or self.FREQUENCY
        values = []
        for i in range(0, self.SAMPLE_RATE):
            value = math.sin(TAU * frequency * (float(i) / self.SAMPLE_RATE)) * (self.VOLUME * self.BIT_DEPTH)
            # Clamp the value as it may go over/under
            value = min(value, (65535 / 2))
            value = max(value, -(65535 / 2))

            for j in xrange(0, self.CHANNELS):
                values.append(value)

        return values

    def squareWave(self, frequency = None):
        frequency = frequency or self.FREQUENCY
        values = []
        for i in range(0, self.sampleLength):
            value = 4 * (math.sin(frequency * (float(i) / self.SAMPLE_RATE)) * (self.VOLUME * self.BIT_DEPTH)) / math.pi
            # Clamp the value as it was going over/under - but now clips
            value = min(value, (65535 / 2))
            value = max(value, -(65535 / 2))

            for j in xrange(0, self.CHANNELS):
                values.append(value)

        return values

    def sawToothWave(self, frequency = None):
        frequency = frequency or self.FREQUENCY
        values = []
        for i in range(0, self.sampleLength):
            value = 2 * (math.sin(frequency * (float(i) / self.SAMPLE_RATE)) * (self.VOLUME * self.BIT_DEPTH)) / -math.pi
            # Clamp the value as it may go over/under
            value = min(value, (65535 / 2))
            value = max(value, -(65535 / 2))

            for j in xrange(0, self.CHANNELS):
                values.append(value)

        return values

