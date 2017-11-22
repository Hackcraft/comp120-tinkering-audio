import wave
import math
import struct

SAMPLE_WIDTH = 2
SAMPLE_RATE = 44100
BIT_DEPTH = 65535 / 2
CHANNELS = 2
DURATION = 5  #seconds
VOLUME = 0.4
TAU = math.pi * 2
FREQUENCY = 150 #Hz
sampleLength = SAMPLE_RATE * DURATION

def funGenerateSingleWave():
    noiseOut = wave.open("wave.wav","w")  # open file wave.wav in write mode... as file does not exist it will be created
    noiseOut.setnchannels(CHANNELS)
    noiseOut.setsampwidth(SAMPLE_WIDTH)
    noiseOut.setframerate(SAMPLE_RATE)

    values = []

    for i in xrange(0, sampleLength):
        value = math.sin(TAU * FREQUENCY * (float(i) / SAMPLE_RATE)) * (VOLUME * BIT_DEPTH)
        data = struct.pack('<h', value)  # <h = short?

        for j in xrange(0, CHANNELS):
            values.append(data)
    noiseOutString = ''.join(values)
    print noiseOutString
    noiseOut.writeframes(noiseOutString)
    return values

def funCombineTones(toneOne, toneTwo, sampleLength):
    values = []
    for i in xrange(0, sampleLength):
        values.append(toneOne[i] + toneTwo[i])
    return values

def funEcho(soundOne, delay, sampleLength):
    values = []
    for i in xrange (0, sampleLength):
        values.append(soundOne[i])
        if i > delay:
            echo = soundOne[i]*0.6
            values.append(echo+soundOne[i])
    return values
def funCreateEchoWave(sound, echo):
    noiseOut = wave.open("echo.wav","w")  # open file wave.wav in write mode... as file does not exist it will be created
    noiseOut.setnchannels(CHANNELS)
    noiseOut.setsampwidth(SAMPLE_WIDTH)
    noiseOut.setframerate(SAMPLE_RATE)
    values = []
    values = funCombineTones(sound, echo, sampleLength)
    noiseOutString = ''.join(values)
    print noiseOutString
    noiseOut.writeframes(noiseOutString)

tone = funGenerateSingleWave()
funEcho(wave.wav, )
funCreateEchoWave()