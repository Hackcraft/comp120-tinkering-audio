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

        test = self.notes.createNote("A")
        soundFunctions.saveWaveFile("test.wav", test, self.notes.SAMPLE_RATE, self.notes.CHANNELS, self.notes.SAMPLE_WIDTH)