from soundFunctions import *
from notes import *

soundFunctions = SoundFunctions()

class Tunes:

    def __init__(self):
        print "Loaded Tunes"
        self.notes = Notes()

        test = self.notes.createNote("A#2", 0)
        test2 = self.notes.createNote("E", 1)
        test3 = self.notes.createNote("E", 2)

        soundFunctions.saveWaveFile("test.wav", test, self.notes.variables)
        soundFunctions.saveWaveFile("test2.wav", test2, self.notes.variables)
        soundFunctions.saveWaveFile("test3.wav", test3, self.notes.variables)

"""""
    def arrayToTune(self, array, defaults):
        values = []
        objects = []

        # Setup default note class
        objects.append(

        )

        # Go through each note
        for note in array:
            if note
"""

