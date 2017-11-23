import wave
import math
import struct

from soundFunctions import *
from notes import *

soundFunctions = SoundFunctions()

class Tunes:

    def __init__(self):
        print "Loaded Tunes"
        self.notes = Notes()

        test = self.notes.createNote("A#2", 0)
        test2 = self.notes.createNote("A#2", 1)
        test3 = self.notes.createNote("A#2", 2)

        soundFunctions.saveWaveFile("test.wav", test, self.notes.SAMPLE_RATE, self.notes.CHANNELS, self.notes.SAMPLE_WIDTH)
        soundFunctions.saveWaveFile("test2.wav", test2, self.notes.SAMPLE_RATE, self.notes.CHANNELS, self.notes.SAMPLE_WIDTH)
        soundFunctions.saveWaveFile("test3.wav", test3, self.notes.SAMPLE_RATE, self.notes.CHANNELS, self.notes.SAMPLE_WIDTH)