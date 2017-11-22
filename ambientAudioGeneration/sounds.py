import wave
import math
import struct
TAU = math.pi * 2
class Sounds:

    def __init__(self):
        self.data = []
        self.SAMPLE_WIDTH = 2
        self.SAMPLE_RATE = 44100
        self.BIT_DEPTH = 65535 / 2
        self.CHANNELS = 2
        self.DURATION = 5  # seconds
        self.VOLUME = 0.4
        self.FREQUENCY = 150  # Hz
        self.sampleLength = self.SAMPLE_RATE * self.DURATION
        self.addedSounds = -1

    def setValues(self, sampleWidth, sampleRate, bitDepth, channels, duration, volume, frequency):
        self.SAMPLE_WIDTH = sampleWidth
        self.SAMPLE_RATE = sampleRate
        self.BIT_DEPTH = bitDepth
        self.CHANNELS = channels
        self.DURATION = duration
        self.VOLUME = volume
        self.FREQUENCY = frequency
        self.sampleLength = self.SAMPLE_RATE * self.DURATION

    def makeSound(self, path):
        # open file wave.wav in write mode... as file does not exist it will be created
        try:
            noiseOut = wave.open(path, "w")
        except ValueError:
            print ValueError
            return -1
        noiseOut.setnchannels(self.CHANNELS)
        noiseOut.setsampwidth(self.SAMPLE_WIDTH)
        noiseOut.setframerate(self.SAMPLE_RATE)

        values = []

        for i in xrange(0, self.sampleLength):
            value = math.sin(TAU * self.FREQUENCY * (float(i) / self.SAMPLE_RATE)) * (self.VOLUME * self.BIT_DEPTH)
            data = struct.pack('<h', value)  # <h = short?

            for j in xrange(0, self.CHANNELS):
                values.append(data)

        noiseOutString = ''.join(values)
        noiseOut.writeframes(noiseOutString)

        self.data.append(noiseOut) # save the sound
        self.addedSounds += 1
        return self.addedSounds

    def playSound(self, num):
        if num > self.addedSounds:
            print "Sound " + str(num) + " not found!"

        print "Playing!"
        # play audio



