import pygame

# For each loop - change volume
def change_volume(samples, volume_change):
    for sample in explosion_samples:
        sample *= volume_change  # *2 - Doubles sound

pygame.init()
pygame.mixer.init()

pygame.display.set_mode((800, 600))

# Instead of playing at start, start/stop on key press
# sfxr - tool to generate sound
# Only for music, can only play one at once
pygame.mixer.music.load('testsound.mp3')
pygame.mixer.music.play()

# Sound, individual sound effects
explosion_sound = pygame.mixer.Sound('explosion.wav')

# Raw sound
explosion_samples = pygame.sndarray.samples(explosion_sound)

# Next week saving and further malipulation
# Do exercise 1 + 2 on week 7 slides - before next week

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                explosion_sound.play()
            if event.key == pygame.K_UP:
                change_volume(explosion_samples, 2) # Check samples to stop clipping
            if event.key == pygame.K_UP:
                change_volume(explosion_samples, 0.5) # Won't work because float

    pygame.display.update()

pygame.quit()