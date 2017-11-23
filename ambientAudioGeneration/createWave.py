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

    def sineWave(self, frequency = None, sampleRate = None, sampleLength = None, volume = None):
        frequency = frequency or self.FREQUENCY
        sampleRate = sampleRate or self.SAMPLE_RATE
        sampleLength = sampleLength or self.SAMPLE_RATE
        volume = volume or self.VOLUME

        values = []
        for i in range(0, sampleLength):
            value = math.sin(TAU * frequency * (float(i) / sampleRate)) * (volume * self.BIT_DEPTH)
            for j in xrange(0, self.CHANNELS):
                values.append(value)

        return values

    def squareWave(self, frequency = None, sampleRate = None, sampleLength = None, volume = None):
        frequency = frequency or self.FREQUENCY
        sampleRate = sampleRate or self.SAMPLE_RATE
        sampleLength = sampleLength or self.sampleLength
        volume = volume or self.VOLUME

        values = []
        for i in range(0, sampleLength):
            value = 4 * (math.sin(frequency * (i / sampleRate)) * (volume * self.BIT_DEPTH)) / math.pi

            for j in xrange(0, self.CHANNELS):
                values.append(value)

        return values

    def sawToothWave(self, frequency, sample_rate, sample_length, volume):
        values = []
        for i in range(0, sample_length):
            value = 2 * (math.sin(frequency * (i / sample_rate)) * (volume * BIT_DEPTH)) / -math.pi

            for j in xrange(0, CHANNELS):
                values.append(value)

        return values

