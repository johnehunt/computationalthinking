import pygame

print('Initializing system')
# Initialise play game and the sound system
pygame.init()
pygame.mixer.init()

print('Play sound')
# Load the sound file and play it once
pygame.mixer.music.load('bensound-epic.mp3')
pygame.mixer.music.play() # -1 to loop

print('Done')
