import pygame,numpy, struct, wave, math


tau = 2 * numpy.pi

width = 800
height = 600

sample_rate = 44100
channels = 1
duration = 5 # seconds
sample_length = sample_rate * duration
frequency = 150 #Hz
volume = 0.4
bit_depth = 65535 / 2


#pygame.display.set_mode((width, height))
noise_out = wave.open("wave.wav", "w") # open file wave.wav in write mode... as file does not exist it will be created
noise_out.setnchannels(channels)
noise_out.setsampwidth(2)
noise_out.setframerate(sample_rate)

values = []

for i in xrange (0, sample_length):
    value = math.sin(2.0 * math.pi * frequency * (float(i) / sample_rate)) * (volume * bit_depth)
    data = struct.pack('<h', value) # <h = short?

    for j in xrange(0, channels):
        values.append(data)

noise_out_string = ''.join(values)
print noise_out_string
noise_out.writeframes(noise_out_string)