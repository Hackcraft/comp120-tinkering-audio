import wave
import math
import struct

from createWave import *

class Notes:

    def __init__(self):
        print "Loaded Notes"
        self.SAMPLE_WIDTH = 2
        self.SAMPLE_RATE = 44100
        self.BIT_DEPTH = 65535 / 2
        self.CHANNELS = 2
        self.DURATION = 1  # seconds
        self.VOLUME = 0.4
        self.FREQUENCY = 150  # Hz
        self.sampleLength = self.SAMPLE_RATE * self.DURATION
        self.noteToNumbers = {
            "A" : 0,
            "A2" : 12,
            "A#" : 1,
            "A#2" : 13,
            "B" : 2,
            "B2" : 14,
            "C" : -9,
            "C2" : 3,
            "C3" : 15,
            "C#" : -8,
            "C#2" : 4,
            "D" : -7,
            "D2" : 5,
            "D#" : -6,
            "D#2" : 6,
            "E" : -5,
            "E2" : 7,
            "F" : -4,
            "F2" : 8,
            "F#" : -3,
            "F#2" : 9,
            "G" : -2,
            "G2" : 10,
            "G#" : -1,
            "G#2" : 11,
        }
        self.createWave = CreateWave()
        self.updateCreateWave() # Update wave creator

    def setValues(self, sampleWidth, sampleRate, bitDepth, channels, duration, volume, frequency):
        self.SAMPLE_WIDTH = sampleWidth
        self.SAMPLE_RATE = sampleRate
        self.BIT_DEPTH = bitDepth
        self.CHANNELS = channels
        self.DURATION = duration
        self.VOLUME = volume
        self.FREQUENCY = frequency
        self.sampleLength = self.SAMPLE_RATE * self.DURATION
        self.updateCreateWave()  # Update wave creator

    def updateCreateWave(self):
        # Update wave generator
        self.createWave.setValues(
            self.SAMPLE_WIDTH,
            self.SAMPLE_RATE,
            self.BIT_DEPTH,
            self.CHANNELS,
            self.DURATION,
            self.VOLUME,
            self.FREQUENCY
        )

    def createNote(self, note):
        if not str.isdigit(note):
            if note in self.noteToNumbers:
                note = self.noteToNumbers[note]
            else:
                raise ValueError('createNote in class notes expected number or note. Given ' + str(type(note)))

        frequency = 44.0 * 2 ** (note / 12.0)

        return self.createWave.sineWave(frequency)
