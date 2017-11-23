import wave
import math
import struct

class SoundFunctions:

    def __init__(self):
        print "Loaded SoundFunctions"

    def combineTones(self, toneOne, toneTwo, sampleLength):
        values = []
        for i in range(0, sampleLength):
            values.append(toneOne[i] + toneTwo[i])
        return values

    def makeChord(self, sound1, sound2, sound3, sampleLength):
        values = []
        for i in range(0, sampleLength):
            values.append(sound1[i])
            if i > 4000:
                values.append(sound1[i] + sound2[i])
            if i > 8000:
                values.append(sound1[i] + sound2[i] + sound3[i])

        return values

    def echo(self, sound1, sound2, delay, sampleLength):
        values = []
        for i in range(0, sampleLength):
            values.append(sound1[i])
            if i > delay:
                echo = sound1[i] * 0.6
                values.append(echo + sound1[i])
        return values

    def saveWaveFile(self, filename, wavData, sampleRate, channels, sampleWidth):
        packedValues = []
        for i in range(0, len(wavData)):
            packedValue = struct.pack('h', wavData[i])
            packedValues.append(packedValue)

        noiseOut = wave.open(filename, 'w')
        noiseOut.setparams((channels, sampleWidth, sampleRate, 0, 'NONE', 'not compressed'))
        valueStr = ''.join((str(n) for n in packedValues))
        noiseOut.writeframes(valueStr)
        noiseOut.close()

