import wave
import math
import struct

from createWave import *
from soundVariables import *


class Notes:

    def __init__(self):
        print "Loaded Notes"
        self.variables = SoundVariables()
        # The numbers to calculate with frequency for the given note
        self.noteToNumbers = {
            "A": 0,
            "A2": 12,
            "A#": 1,
            "A#2": 13,
            "B": 2,
            "B2": 14,
            "C": -9,
            "C2": 3,
            "C3": 15,
            "C#": -8,
            "C#2": 4,
            "D": -7,
            "D2": 5,
            "D#": -6,
            "D#2": 6,
            "E": -5,
            "E2": 7,
            "F": -4,
            "F2": 8,
            "F#": -3,
            "F#2": 9,
            "G": -2,
            "G2": 10,
            "G#": -1,
            "G#2": 11,
        }
        self.createWave = CreateWave()

    def setValues(self, values):
        self.variables.setValues(values)
        # Keep the CreateWave class in sync with this
        self.createWave.setValues(values)

    def createNote(self, note, wave = 0):
        # Check for valid note
        if not str.isdigit(note):
            if note in self.noteToNumbers:
                note = self.noteToNumbers[note]
            else:
                raise ValueError('createNote in class Notes, expected number or note. Given ' + str(type(note)))

        # Frequency of the given note
        frequency = 44.0 * 2 ** (note / 12.0)

        # Run the wanted wave generation algorithm with specified note, return the output
        return self.createWave.makeWave(wave, frequency)
