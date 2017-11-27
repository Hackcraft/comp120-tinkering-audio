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

        soundData = SoundVariables()
        tune = self.arrayToTune([
            ("A", 1),
            ("B", 1),
            ("C", 1),
            ("D", 1),
            ("E", 1),
            ("F", 1),
            ("G", 1),
        ],
            soundData
        )

        soundFunctions.saveWaveFile("test4.wav", tune, soundData)


    def arrayToTune(self, array, soundData):
        values = []

        # Go through each note
        for note in array:
            if len(note) >= 3: # If given new sound data, update
                self.notes.setValues(note[2])
            block = self.notes.createNote(note[0], 1)
            for bit in block:
                values.append(bit)

        return values




